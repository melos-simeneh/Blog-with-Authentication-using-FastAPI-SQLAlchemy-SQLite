from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import models
from schemas import schemas
from database import engine,SessionLocal
from utils import Hash
from routes import blog, user,auth

app=FastAPI(
    docs_url="/",
    title="Blog Fast API Documentation",
    description="Blog Fast API documentation"
)
 
models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)