from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Model(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/")
def create_model(model: Model):
    return model

@app.get("/health")
def health_check():
    return {"status": "ok"}