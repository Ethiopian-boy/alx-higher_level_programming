#!/usr/bin/python3
"""
Time for an interview!
list 10 commits (from the most recent to oldest) of the repository
You must use the GitHub API,
"""

import requests
from sys import argv


if __name__ == "__main__":
    owner = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner, repo)
    req = requests.get(url)
    commits_json = req.json()
    for commit in commits_json[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
