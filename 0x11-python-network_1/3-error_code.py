#!/usr/bin/python3
""" This script takes in an url, sends a request to the
url and displays the body of the response """
from urllib import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            data = response.read()

            data = data.encode('utf-8')

        print(data)

    except HTTPError as e:
        print(f"Error code: {e.code}")
