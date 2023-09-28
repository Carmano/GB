from fastapi import FastAPI
from models import users, orders,  metadata, engine, database


metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/create_fake_users/{count}')
async def create_fake_user(count: int):
    for i in range(count):
        query = users.insert().values()
        await database.execute(query)
    return count

