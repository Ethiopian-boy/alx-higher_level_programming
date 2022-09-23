#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse header
Response header value
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
