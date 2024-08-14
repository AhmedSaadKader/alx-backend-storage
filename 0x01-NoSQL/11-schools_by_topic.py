#!/usr/bin/env python3
"""Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of all documents with the topic [topic] in [mongo_collection]"""
    return list(mongo_collection.find({"topic": topic}))
