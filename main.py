from fastapi import FastAPI,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session

from models import models
from schemas import schemas
from database import engine,SessionLocal

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

@app.get('/api/blogs')
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

@app.get('/api/blogs/{id}',status_code=status.HTTP_200_OK)
def get_blog(id,response:Response,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"status":"fail","message":"Blog not found"}
    return blog