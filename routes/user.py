from fastapi import APIRouter
from fastapi import Depends,status
from sqlalchemy.orm import Session
from schemas import schemas
from database import get_db
from typing import List
from controllers import user

router=APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

@router.post('/', status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
def get_user(id:int,db: Session=Depends(get_db)):
    return user.get_user(id,db)

@router.get('/', status_code=status.HTTP_200_OK,response_model=List[schemas.UserResponse])
def get_all_users(db: Session=Depends(get_db)):
    return  user.get_all_users(db)