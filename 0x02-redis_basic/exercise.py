#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from uuid import uuid4


class Cache():
  """Cach class"""

  def __init__(self):
      self._redis = redis.Redis()
      self._redis.flushdb()

  def store(data):
      key = str(uuid4())
      self._redis.set(key, data)