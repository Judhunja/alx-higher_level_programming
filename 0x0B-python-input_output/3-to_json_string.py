#!/usr/bin/python3
""" This module contains a to_json_string function """
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string

    Args:
        my_obj(object): object to obtain JSON representation

    Returns:
        str: the JSON representation of the object
    """
    return json.dumps(my_obj)
