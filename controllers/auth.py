from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from utils.password import Hash
from utils.token import create_access_toekn

def login(request: schemas.Login,db: Session):
    user=db.query(models.User).filter(models.User.username==request.username).first()
    if not user or not Hash.verify_password(request.password,user.password):
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Incorrect username or password",
             headers={"WWW-Authenticate": "Bearer"}
             )
    access_token=create_access_toekn(data={"sub":user.username})
    return {"access_token":access_token,"token_type":"bearer"}