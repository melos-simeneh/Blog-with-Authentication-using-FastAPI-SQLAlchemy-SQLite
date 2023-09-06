from fastapi import APIRouter
from schemas import schemas
from fastapi import APIRouter
from fastapi import Depends,status
from sqlalchemy.orm import Session
from schemas import schemas
from database import get_db
from typing import List
from controllers import blog


router=APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post('/login')
def login(request: schemas.Login,db: Session=Depends(get_db)):
    return
