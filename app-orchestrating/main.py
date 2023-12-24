# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World app orchestrating"}


@app.get("/orchestrating/hello")
def read_hello():
    return {"Hello": "World from app-orchestrating"}