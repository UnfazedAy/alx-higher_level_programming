#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""


import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
