from pydantic import BaseModel, Field
from typing import Optional
import databases
import sqlalchemy


DATABASE_URL = 'sqlite:///./app.db'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(32)),
    sqlalchemy.Column('last_name', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(32)),
    sqlalchemy.Column('password', sqlalchemy.String(32)),
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('id_user', sqlalchemy.Integer),
    sqlalchemy.Column('id_product', sqlalchemy.Integer),
    sqlalchemy.Column('date_ordered', sqlalchemy.Date),
    sqlalchemy.Column('str', sqlalchemy.String(32)),
)
#
products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('description', sqlalchemy.String(32)),
    sqlalchemy.Column('price', sqlalchemy.Float),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class User(BaseModel):
    id: int
    first_name: str = None
    last_name: str = None
    address: str = None
    email: str = None
    password: str = None


class Order(BaseModel):
    id: int = Field()
    id_user: int = Field()
    id_product: int = Field()
    date_ordered: str = Field()
    status: Optional[str] = Field()


class Product(BaseModel):
    id: int = Field()
    name: str = Field()
    description: str = Field()
    price: float = Field()







