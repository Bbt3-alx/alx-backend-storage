#!/usr/bin/env python3
"""Log stats"""


import pymongo
from pymongo import MongoClient


def log_stats():
    """A script that provides some stats about Nginx logs stored in MongoDB"""
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


if __name__ == "__main__":
    log_stats()
