#!/usr/bin/python3
""" This script prints the X-Request-Id in the response
header after a request has been made """
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])

    print(req.headers.get('X-Request-Id'))
