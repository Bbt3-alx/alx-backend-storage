#!/usr/bin/python3
""" Test file """
from pymongo import MongoClient
import random
import time
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.tmp_db_4.tmp_col_4
    
    obj_by_id = {}
   
    # create all documents
    objs = []
    for i in range(5):
        obj_d = { 
            'name': "Obj {}".format(i)
        }
        
        objs.append(obj_d)
    
    # generate match
    match_name = "match_name"
    for obj in random.sample(objs, 3):
        obj['name'] = match_name
    
    # insert all documents
    for obj in objs:
        obj_id = str(col.insert_one(obj).inserted_id)
        obj_by_id[obj_id] = obj

    # update dictionary
    new_topics = ["new topic 0", "new topic 1"]
    for k in obj_by_id.keys():
        obj = obj_by_id.get(k)
        if obj.get('name') == match_name:
            obj['topics'] = new_topics[:]
            obj_by_id[k] = obj

    time.sleep(2)
    
    # update
    update_topics(col, match_name, new_topics)

    time.sleep(2)
    
    # validate update
    items = col.find()
    for item in items:
        i_id = str(item.get('_id'))
        obj = obj_by_id.get(i_id)
        
        if obj is None:
            print("{} not found".format(i_id))
            exit(0)
        
        # check name
        if item.get('name') != obj.get('name'):
            print("Not the same object: {} / {}".format(item, obj))
            exit(0)

        # check topics
        obj_topics = obj.get('topics', [])
        item_topics = item.get('topics', [])
        if len(obj_topics) != len(item_topics):
            print("No the same list of topics: {} / {}".format(item, obj))
            exit(0)

        for item_topic in item_topics:
            if item_topic in obj_topics:
                obj_topics.remove(item_topic)
        if len(obj_topics) != 0:
            print("No the same list of topics: {} / {}".format(item, obj))
            exit(0)

        del obj_by_id[i_id]
        
    if len(obj_by_id) == 0:
        print("OK", end="")
        exit(0)
    print("Documents not updated: {}".format(obj_by_id))
