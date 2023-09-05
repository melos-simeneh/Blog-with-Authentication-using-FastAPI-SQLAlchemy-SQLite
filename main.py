from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from models import model
from schemas import schema
from database import engine,SessionLocal

app=FastAPI(
    docs_url="/",
    title="Blog Fast API Documentation",
    description="Blog Fast API documentation"
)

model.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try: 
     yield db
    finally:
        db.close()

@app.get('/api/blogs')
def get_all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(model.Blog).all()
    return blogs

@app.post('/api/blogs')
def create_blog(request:schema.Blog,db:Session=Depends(get_db)):
    new_blog=model.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/api/blogs/{id}')
def get_blog(id,db:Session=Depends(get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id).first()
    return blog