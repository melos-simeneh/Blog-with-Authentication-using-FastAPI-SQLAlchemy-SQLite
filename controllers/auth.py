from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from utils.password import Hash
from utils.token import create_access_token


def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.username == request.username).first()

    if not user or not Hash.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = create_access_token(data={"sub": user.username, "user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}