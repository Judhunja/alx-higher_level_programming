#!/usr/bin/python3
""" This module contains a from_json_string function """
import json


def from_json_string(my_str):
    """
    Decodes a JSON representation of a python object

    Args:
        my_str(sting): string to be decoded

    Returns:
        (object): python object
    """
    return json.loads(my_str)
