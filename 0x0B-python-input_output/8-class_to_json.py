#!/usr/bin/python3
""" This module contains a class_to_json function """


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure for JSON serialization(the values it returns can
    be serialized to JSON) of an object

    Args:
        obj: class instance

    Returns:
        dict: dict representation of the object's attributes
    """
    return vars(obj)
