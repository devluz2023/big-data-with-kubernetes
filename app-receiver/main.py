# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World receiver updated"}


@app.get("/app-receiver/hello")
def read_hello():
    return {"Hello": "World from app-receiver"}