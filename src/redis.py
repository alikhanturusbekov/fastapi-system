from pydantic import BaseModel
from redis import Redis

redis_client: Redis | None = None


class RedisData(BaseModel):
    key: str
    value: str
    ttl: int | None


def get_client() -> Redis:
    return redis_client


async def set_redis_key(redis_data: RedisData):
    async with redis_client.pipeline(transaction=False) as pipe:
        await pipe.set(redis_data.key, redis_data.value)
        if redis_data.ttl:
            await pipe.expire(redis_data.key, redis_data.ttl)

        await pipe.execute()


async def get_by_key(key: str):
    return await redis_client.get(key)


async def delete_by_key(key: str):
    return await redis_client.delete(key)
