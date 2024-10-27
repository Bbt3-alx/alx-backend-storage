#!/usr/bin/env python3
"""Log stats"""


import pymongo
from pymongo import MongoClient


def log_stats():
    """A script that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017')
    nginx = client.logs.nginx

    if nginx.count_documents({}) == 0:
        return

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


if __name__ == "__main__":
    log_stats()
