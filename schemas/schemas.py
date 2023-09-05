from pydantic import BaseModel

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

    
class BlogResponse(BaseModel):
    id:int
    title:str
    body: str
    creator:UserResponse
    
