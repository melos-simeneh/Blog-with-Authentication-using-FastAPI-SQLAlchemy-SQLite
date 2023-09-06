from fastapi import APIRouter
from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from database import engine,SessionLocal,get_db
from utils import Hash
from typing import List

router=APIRouter(
    prefix="/api/users",
    tags=["Users"]
)



@router.post('/', status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    new_user=models.User(name=request.name,username=request.username,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
def get_user(id,db: Session=Depends(get_db)):
    user=db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@router.get('/', status_code=status.HTTP_200_OK,response_model=List[schemas.UserResponse])
def get_all_users(db: Session=Depends(get_db)):
    users=db.query(models.User).all()
    return  users