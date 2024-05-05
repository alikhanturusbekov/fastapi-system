from fastapi import APIRouter

from src import service
from src import redis

router = APIRouter()


@router.post('/')
async def insert_example(example_id: int, title: str):
    return await service.insert(example_id, title)


@router.patch('/')
async def update_example_by_id(example_id: int, title: str):
    return await service.update(example_id, title)


@router.get('/')
async def get_all():
    return await service.get_all()


@router.get('/{example_id}')
async def get_example_by_id(example_id: int):
    return await service.get_by_id(example_id)


@router.delete('/{example_id}')
async def delete_example_by_id(example_id: int):
    return await service.delete(example_id)


@router.post('/redis/')
async def create_redis_data(redis_data: redis.RedisData):
    return await redis.set_redis_key(redis_data)


@router.get('/redis/{key}')
async def get_redis_data(key: str):
    return await redis.get_by_key(key)


@router.delete('/redis/{key}')
async def get_redis_data(key: str):
    return await redis.delete_by_key(key)



