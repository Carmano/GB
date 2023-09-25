from fastapi import FastAPI
from models import Item

app = FastAPI()


@app.get('/')
async def root():
    return "<h1>Hello</h1>"


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, "q": q}


@app.post('/items/')
async def create_item(item: Item):
    return item

# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'
