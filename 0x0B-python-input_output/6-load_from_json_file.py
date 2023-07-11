#!/usr/bin/python3
""" This module contains a load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file
    Args:
        filename(string): file containing JSON objects
    """
    with open(filename, encoding="utf-8") as json_f:
        return json.load(json_f)
