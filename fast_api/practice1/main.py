from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/amir")
def call_amir():
    return "I AM AMIR"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item id: ":item_id, "q: ":q}


@app.post("/items/")
def create_item(item: Item):
    return item