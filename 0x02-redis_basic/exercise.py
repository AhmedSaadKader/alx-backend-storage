#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from uuid import uuid4
from typing import Callable, Optional, Union


class Cache():
  """Cach class"""

  def __init__(self):
      self._redis = redis.Redis()
      self._redis.flushdb()

  def store(self, data: Union[str, bytes, int, float]) -> str:
      key = str(uuid4())
      self._redis.set(key, data)
      return key

  def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
      """Get data from cache"""
      if fn:
          return fn(self._redis.get(key))
      return self._redis.get(key)

  def get_str(self, key: str) -> str:
      return self._redis.get(key).decode('utf-8')

  def get_int(self, key:str) -> int:
      value = self._redis.get(key)
      try:
          value = int(value.decode('utf-8'))
      except Exception:
          value = 0
      return value
