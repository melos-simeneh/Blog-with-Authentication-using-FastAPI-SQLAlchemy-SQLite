from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from utils.password import Hash

def create_user(request: schemas.User, db: Session):
    existing_user = db.query(models.User).filter(models.User.username == request.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    hashed_password = Hash.hash_password(request.password)

    new_user = models.User(name=request.name, username=request.username, password=hashed_password)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user due to an internal error"
        )


def get_user(id:int,db: Session):
    user=db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

def get_all_users(db: Session):
    users=db.query(models.User).all()
    return  users