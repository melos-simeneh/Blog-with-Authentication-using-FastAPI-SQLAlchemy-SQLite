from fastapi import FastAPI

app=FastAPI()

@app.get('/api/')
async def get():
    return {"message":"Hello, world!"}