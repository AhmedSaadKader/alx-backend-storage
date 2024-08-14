#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis


class Cache():
  """Cach class"""

  def __init__(self):
    self._redis = redis.Redis()
    self._redis.flushdb()
