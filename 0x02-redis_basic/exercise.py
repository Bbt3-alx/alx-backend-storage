#!/usr/bin/env python3
"""Writing string to Redis"""


from typing import Callable, Optional, Union
import redis
import uuid
import functools


def call_history(method: Callable) -> callable:
    """Decorator to store the history of inputs and outputs for a function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store inputs and outputs in Redis"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output
    return wrapper

def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to increment call count and call the
        original method
        """
        key = f"{method.__qualname__}:calls"

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Class to handle caching operations with Redis"""
    def __init__(self):
        """Instatiate the class Cache and connect to Redis"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
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
    @call_history
    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[int, str, float, bytes, None]:
        """Retrieve data from Redis and optionally convert it using fn"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as integer"""
        return self.get(key, lambda x: int(x))
