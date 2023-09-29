#!/usr/bin/python3
""" This script prints the X-Request-Id in the response
header after a request has been made """
import requests
from sys import argv


if __name__ == "__main__":
    post = requests.post(argv[1], data={'email': argv[2]})

    print(post.text)
