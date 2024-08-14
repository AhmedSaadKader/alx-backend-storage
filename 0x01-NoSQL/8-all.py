#!/usr/bin/env python3
"""List all document in Python
"""


def list_all(mongo_collection):
    """lists all documents in mongo_collection"""
    return mongo_collection.find()
