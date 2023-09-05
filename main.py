from fastapi import FastAPI
from models import model
from schemas import schema
from database import engine

app=FastAPI(
    docs_url="/",
    title="Blog Fast API Documentation",
    description="Blog Fast API documentation"
)

model.Base.metadata.create_all(engine)

@app.get('/api/blogs')
def get_all_blogs(request:schema.Blog):
    return {"message":"Hello, world!"}