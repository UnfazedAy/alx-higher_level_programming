#!/usr/bin/python3
"""
Sending a post request using requests package
"""


from sys import argv
import requests
if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    post_doc = requests.post(url, email=email)
    print(post_doc.text)
