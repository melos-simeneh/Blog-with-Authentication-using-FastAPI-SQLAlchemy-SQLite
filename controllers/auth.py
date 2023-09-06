from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from utils.bcrypt import Hash

def login(request: schemas.Login,db: Session):
    user=db.query(models.User).filter(models.User.username==request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not Hash.verify_password(request.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect username or password",)
    
    return "Correct"