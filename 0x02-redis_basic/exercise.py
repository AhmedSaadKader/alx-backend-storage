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
  