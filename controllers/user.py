from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from utils.password import Hash

def create_user(request:schemas.User, db: Session):
    new_user=models.User(name=request.name,username=request.username,password=Hash.hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int,db: Session):
    user=db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

def get_all_users(db: Session):
    users=db.query(models.User).all()
    return  users