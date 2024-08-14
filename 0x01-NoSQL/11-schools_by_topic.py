#!/usr/bin/env python3
"""Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find({"topic": topic}))
