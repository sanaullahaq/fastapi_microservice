from typing import List
from fastapi import FastAPI

from app.crud import create_items, get_items
from app.models import Item, items
from app.schemas import ItemCreate


app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/items/', response_model=List[Item])
def read_items():
    return get_items()


@app.post('/items/', response_model=Item)
def add_item(item: ItemCreate):
    new_item = Item(id=len(items)+1, **item.dict())
    return create_items(new_item)