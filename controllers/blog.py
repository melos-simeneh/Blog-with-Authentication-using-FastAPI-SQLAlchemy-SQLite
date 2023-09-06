from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def get_all_blogs(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create_blog(request,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(id:int,db:Session):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog

def update_blog(id:int,request: schemas.Blog,db:Session):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    blog.title=request.title
    blog.body=request.body
    db.commit()
    db.refresh(blog)
    return "blog updated"

def delete_blog(id:int, db: Session):
    blog = db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return