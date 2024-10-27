def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.
    
    Parameters:
    - mongo_collection: the pymongo collection object
    - name (string): the school name to update
    - topics (list of strings): the list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
