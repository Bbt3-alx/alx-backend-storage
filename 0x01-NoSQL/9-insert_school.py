#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """insert a new doc in a collection"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
