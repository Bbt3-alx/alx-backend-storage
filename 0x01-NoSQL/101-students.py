#!/usr/bin/env python3
"""Top Students"""


def top_students(mongo_collection):
    """ A  function that returns all students sorted by average score """
    pipeline = [
            {"$unwind": "$topics"},
            {"$group": {"_id": "$name", "averageScore": {
                "$avg": "$topics.score"
                }}},
            {"$project": {
                "name": "$_id",
                "averageScore": 1,
                "_id": 0
            }},
            {"$sort": {"averageScore": -1}}
        ]

    result = mongo_collection.aggregate(pipeline)

    return result

