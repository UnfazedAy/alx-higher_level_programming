#!/usr/bin/python3
"""A script that takes in url,
sends a request to the url and displays
the body of the response decoded in utf-8 as well as manage error"""


from urllib.request import urlopen, Request
from sys import argv
form urllib.error import HTTPError, URLError
if __name__ == '__main__':
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read.decode('utf-8')
    except HTTPError as error:
        print("Error code: {}".format(error.code))

