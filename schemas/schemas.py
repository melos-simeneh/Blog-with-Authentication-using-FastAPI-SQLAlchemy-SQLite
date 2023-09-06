from pydantic import BaseModel
from typing import Optional

# This is API related
class Blog(BaseModel):
    title:str
    body: str    

class User(BaseModel):
    name:str
    username:str
    password:str


class UserResponse(BaseModel):
    id:int
    name:str
    username:str
    blogs:list[Blog]

class UserResponseWithoutBlogs(BaseModel):
    name: str
    username: str
class BlogResponse(BaseModel):
    # id:int
    title:str
    body: str
    creator: Optional[UserResponseWithoutBlogs] = None

    

    
