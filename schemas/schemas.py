from pydantic import BaseModel

# This is API related
class Blog(BaseModel):
    title:str
    body: str
    
class BlogResponse(BaseModel):
    title:str
    body: str