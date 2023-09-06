from fastapi import APIRouter
from schemas import schemas
from fastapi import APIRouter
from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from database import engine,SessionLocal,get_db
from utils import Hash
from typing import List


router=APIRouter(
    prefix="/api/blogs",
    tags=["Blogs"]
)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.BlogResponse])
def get_all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.BlogResponse)
def create_blog(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.BlogResponse)
def get_blog(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.BlogResponse)
def update_blog(id,request: schemas.Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    blog.title=request.title
    blog.body=request.body
    db.commit()
    db.refresh(blog)
    return "blog updated"

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return

