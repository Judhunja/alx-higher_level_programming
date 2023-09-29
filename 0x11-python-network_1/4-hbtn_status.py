#!/usr/bin/python3
""" This script fetches an URL """
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    body = req.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
