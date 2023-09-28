from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class User(BaseModel):
    username: str
    full_name: str = None


class Order(BaseModel):
    items: List[Item]
    user: User

