#!/usr/bin/python3
""" This script fetches an URL """
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urlopen(req) as response:
        body = response.read()
        body_to_string = body.decode('utf-8')

        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body_to_string}")

    response.close()
