from fastapi import FastAPI
from models import models
from database import engine

from routes import blog, user,auth

app=FastAPI(
    docs_url="/docs",
    title="Blog Fast API Documentation",
    description="This is a Blog API built with FastAPI for managing blogs and users.",  
    version="1.0.0",  
)

models.Base.metadata.create_all(engine)

@app.get("/",include_in_schema=False)
def read_root():
    return {"message": "Welcome to the Blog API!"}

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)