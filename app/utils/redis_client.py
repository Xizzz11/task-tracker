<<<<<<< HEAD
﻿import redis

from app1.core.config import REDIS_URL


def get_redis_client():
    try:
        client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
=======
import redis
import json
from app.core.config import settings

def get_redis_client():
    try:
        client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
        client.ping()
        return client
    except Exception:
        return None

<<<<<<< HEAD

redis_client = get_redis_client()
=======
redis_client = get_redis_client()
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
