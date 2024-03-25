#!/usr/bin/env python3
"""returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """search for the topic and return the school"""
    result_list = mongo_collection.find({"topics": topic})
    return result_list
