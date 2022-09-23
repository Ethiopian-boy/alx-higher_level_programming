#!/usr/bin/python3
"""Error code #1
"""

import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    if (req.status_code < 400):
        print(req.text)
    else:
        print("Error code: {}".format(req.satus_code))
