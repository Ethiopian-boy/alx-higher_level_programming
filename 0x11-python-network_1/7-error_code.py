#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
Error code #1
"""

import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    if (req.status_code >= 400):
        print("Error code: {}".format(req.satus_code))
    else:
        print(req.text)
