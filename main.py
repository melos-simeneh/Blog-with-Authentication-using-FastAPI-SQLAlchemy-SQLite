from fastapi import FastAPI

app=FastAPI()

@app.get('/api/')
def get():
    return {"message":"Hello, world!"}