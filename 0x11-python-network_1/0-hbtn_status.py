#!/usr/bin/python3
""" This script fetches an URL """
from urllib.request import urlopen


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urlopen(req) as response:
        body = response.read()
        body_to_string = body.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body_to_string}")
