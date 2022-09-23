#!/usr/bin/python3
"""
Search API
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv[1]) > 1:
        letter = argv[1]
    else:
        letter = ""
    pyload = {'q': letter}
    req = requests.post(url, data=pyload)
    try:
        json_file = req.json()
        if json_file:
            print("[{}] {}".format(json_file['id'], json_file['name']))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
