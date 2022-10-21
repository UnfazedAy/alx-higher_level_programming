#!/usr/bin/python3
"""A Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """


from urllib.request import urlopen, Request
from sys import argv
from urllib.parse import urlencode
if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(result)
