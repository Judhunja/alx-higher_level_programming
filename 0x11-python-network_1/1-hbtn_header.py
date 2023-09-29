#!/usr/bin/python3
""" This script sends a request to a passed URL and displays
the value of X-Request-Id variable found in the header of
the response """
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        id = response.getheader('X-Request-Id')

    print(id)
