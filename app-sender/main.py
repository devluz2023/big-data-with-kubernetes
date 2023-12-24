# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World app-sender"}


@app.get("/app-sender/hello")
def read_hello():
    return {"Hello": "World from app-sender"}