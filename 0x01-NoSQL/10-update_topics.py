#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Updates school's topics"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
