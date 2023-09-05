from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import models
from schemas import schemas
from database import engine,SessionLocal
from utils import Hash

app=FastAPI(
    docs_url="/",
    title="Blog Fast API Documentation",
    description="Blog Fast API documentation"
)

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try: 
     yield db
    finally:
        db.close()

@app.get('/api/blogs',status_code=status.HTTP_200_OK,response_model=List[schemas.BlogResponse])
def get_all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.post('/api/blogs',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/api/blogs/{id}',status_code=status.HTTP_200_OK,response_model=schemas.BlogResponse)
def get_blog(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog

@app.put('/api/blogs/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request: schemas.Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    blog.title=request.title
    blog.body=request.body
    db.commit()
    db.refresh(blog)
    return "blog updated"

@app.delete('/api/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return


@app.post('/api/users', status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    new_user=models.User(name=request.name,username=request.username,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user