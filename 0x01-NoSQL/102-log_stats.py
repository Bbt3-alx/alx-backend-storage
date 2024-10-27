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

    method_counts = {
        "GET": nginx.count_documents({'method': 'GET'}),
        "POST": nginx.count_documents({'method': 'POST'}),
        "PUT": nginx.count_documents({'method': 'PUT'}),
        "PATCH": nginx.count_documents({'method': 'PATCH'}),
        "DELETE": nginx.count_documents({'method': 'DELETE'}),
    }

    nb_methods = sum(method_counts.values())
    status_check = nginx.count_documents({'path': '/status'})

    print(f"{nb_methods} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
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
