from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# This is database related
class Blog(Base):
    __tablename__ = 'blogs'
    
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))   
    
    creator = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = 'users'
    
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    username=Column(String)
    password=Column(String)
    
    blogs = relationship("Blog", back_populates="creator")