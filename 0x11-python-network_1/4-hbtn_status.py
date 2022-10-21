#!/usr/bin/python3
"""
Using the request package to fetch a url like task 1
"""


import requests
if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
