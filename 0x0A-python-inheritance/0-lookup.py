#!/usr/bin/python3
""" This module contains lookup function """


def lookup(obj):
    """
    looks up the available attributes and methods of an object

    Args:
        obj: object to look up

    Returns:
        a list of availabl attributes and methods of the object
    """
    return dir(obj)


if __name__ == "__main__":
    lookup(obj)
