#!/usr/bin/python3
"""
Using the request package to send a request to the URL
and displays the value of the variable
X-Request-Id in the response header
also sys must be used
"""


from sys import argv
import requests
if __name__ == '__main__':
    url = argv[1]
    my_req = requests.get(url)
    print(my_req.headers.get('X-Request-Id'))
