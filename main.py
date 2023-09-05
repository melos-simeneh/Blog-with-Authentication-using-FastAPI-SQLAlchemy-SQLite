from fastapi import FastAPI

app=FastAPI(
    docs_url="/",
    title="Blog Fast API Documentation",
    description="Blog Fast API documentation"
)

@app.get('/api/blogs')
def get_all_blogs():
    return {"message":"Hello, world!"}