from starlette.config import Config

config = Config('.env')

DATABASE_URL = config('DATABASE_URL', default='postgresql://postgres:postgres@postgres:5432/test')
REDIS_HOST = config('REDIS_HOST', default='redis')
REDIS_PORT = config('REDIS_PORT', default='6379')