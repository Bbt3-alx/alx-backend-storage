#!/usr/bin/env python3
"""Top Students"""


def top_students(mongo_collection):
    """ A  function that returns all students sorted by average score """
    pipeline = [
            {"$unwind": "$topics"},
            {"$group": {"_id": "$name", "averageScore": {
                "$avg": "$topics.score"
                }}},
            {"$sort": {"averageScore": -1}}
        ]

    result = mongo_collection.aggregate(pipeline)

    return list(result)
