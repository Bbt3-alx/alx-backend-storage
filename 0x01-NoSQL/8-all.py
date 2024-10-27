#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """A  function that lists all documents in a collection"""
    all_doc = mongo_collection.find()

    return all_doc
