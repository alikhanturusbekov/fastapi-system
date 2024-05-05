import redis.asyncio as r
from fastapi import FastAPI

from src import redis
from src.config import REDIS_HOST, REDIS_PORT
from src.database import database
from src.router import router

app = FastAPI()


@app.on_event("startup")
async def startup():
    pool = r.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
    redis.redis_client = r.Redis(connection_pool=pool)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await redis.redis_client.close()


app.include_router(router, prefix="/example", tags=["example"])
