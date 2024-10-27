#!/usr/bin/env python3
"""Log stats - new version"""

import pymongo
from pymongo import MongoClient


def log_stat_top_10():
    """
    the top 10 of the most present IPs in the collection nginx
    of the database logs
    """
    client = MongoClient('mongodb://localhost:27017')
    nginx = client.logs.nginx

    nb_methods = nginx.count_documents({})
    nb_get = nginx.count_documents({'method': 'GET'})
    nb_post = nginx.count_documents({'method': 'POST'})
    nb_put = nginx.count_documents({'method': 'PUT'})
    nb_patch = nginx.count_documents({'method': 'PATCH'})
    nb_delete = nginx.count_documents({'method': 'DELETE'})
    status_check = nginx.count_documents({'path': '/status'})

    print(f"{nb_methods} logs")
    print("Methods:")
    print(f"\tmethod GET: {nb_get}")
    print(f"\tmethod POST: {nb_post}")
    print(f"\tmethod PUT: {nb_put}")
    print(f"\tmethod PATCH: {nb_patch}")
    print(f"\tmethod DELETE: {nb_delete}")
    print(f"{status_check} status check")

    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
            ]

    result = nginx.aggregate(pipeline)

    print("IPs:")
    for ip in result:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stat_top_10()
