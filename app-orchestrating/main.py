# main.py
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrumentator setup
Instrumentator().instrument(app).expose(app)



@app.get("/")
def read_root():
    return {"Hello": "World app orchestrating"}


@app.get("/orchestrating/hello")
def read_hello():
    return {"Hello": "World from app-orchestrating"}


