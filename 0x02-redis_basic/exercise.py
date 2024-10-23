#!/usr/bin/env python3
"""Writing string to Redis"""


from typing import Union
import redis
import uuid


class Cache:
    """Class to handle caching operations with Redis"""
    def __init__(self):
        """Instatiate the class Cache and connect to Redis"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[int, bytes, str, float]) -> str:
        """Store data in Redis and return the generated UUID key
        Args:
            data (Union[int, bytes, str, float]): The data to store in Redis.
        Returns:
            str: The UUID key under which the data is stored.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
