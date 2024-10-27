#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    update_all = mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
            )