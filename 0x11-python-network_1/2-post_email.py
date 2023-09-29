#!/usr/bin/python3
""" This script sends a POST request to a passed URL with
email as a parameter, and displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    val = urlencode(val)

    val = val.encode('ascii')

    req = Request(argv[1], val)

    with urlopen(req) as response:
        data = response.read()

        data = data.encode('utf-8')

    print(data)
