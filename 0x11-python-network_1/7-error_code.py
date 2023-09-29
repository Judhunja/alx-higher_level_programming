#!/usr/bin/python3
""" This script sends a request to a passed URL and displays
the body of the respponse. If the status code is greater
than or equal to 400, it prints the error code """
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
        return

    body = req.text

    print(body)
