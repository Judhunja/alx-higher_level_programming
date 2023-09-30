#!/usr/bin/python3
""" This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a
parameter for q, otherwise sends an empty string """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        dat = {"q": ""}
    else:
        dat = {"q": argv[1]}

    pst = requests.post('http://0.0.0.0:5000/search_user', data=dat)

    result = pst.json()
    if result is None:
        print("No result")
    else:
        try:
            print(f'[{result["id"]}] {result["name"]}')
        except Exception:
            print(f"Not a valid JSON")
