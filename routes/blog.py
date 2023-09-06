from fastapi import APIRouter
from schemas import schemas
from fastapi import APIRouter
from fastapi import Depends,status
from sqlalchemy.orm import Session
from schemas import schemas
from database import get_db
from typing import List
from controllers import blog


router=APIRouter(
    prefix="/api/blogs",
    tags=["Blogs"]
)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.BlogResponse])
def get_all_blogs(db:Session=Depends(get_db)):
    return blog.get_all_blogs(db)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.BlogResponse)
def create_blog(request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.create_blog(request, db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.BlogResponse)
def get_blog(id,db:Session=Depends(get_db)):
    return blog.get_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.BlogResponse)
def update_blog(id,request: schemas.Blog,db:Session=Depends(get_db)):
    return blog.update_blog(id,request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db)):
    return blog.delete_blog(id,db)

