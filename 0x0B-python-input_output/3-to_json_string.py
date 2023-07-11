#!/usr/bin/python3
import json
""" This module contains a to_json_string function """


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string

    Args:
        my_obj(object): object to obtain JSON representation
    """
    json_obj = json.dumps(my_obj)

    return json_obj
