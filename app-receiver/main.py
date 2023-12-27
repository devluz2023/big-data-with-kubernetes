from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrumentator setup
Instrumentator().instrument(app).expose(app)



@app.get("/")
def read_root():
    return {"Hello": "World receiver updated"}


@app.get("/app-receiver/hello")
def read_hello():
    return {"Hello": "World from app-receiver"}

@app.get("/app-receiver/sender")
def return_to_sender():
    return {"Hello": "This message come from from app-receiver"}