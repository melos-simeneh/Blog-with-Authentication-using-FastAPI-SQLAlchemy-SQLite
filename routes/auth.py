from fastapi import APIRouter
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers import auth
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(),db: Session=Depends(get_db)):
    return auth.login(request,db)
