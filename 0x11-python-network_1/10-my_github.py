#!/usr/bin/python3
"""
A module that gets your id form github
argv[1] --> username
argv[2] --> token or password
In my case token
"""


import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    response = requests.get(
            'https://api.github.com/user', auth=(username, password))
    data = response.json()
    print(data.get('id'))
