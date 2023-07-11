#!/usr/bin/python3
""" This module contains save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using a
    JSON representation

    Args:
        my_obj(object): objrct to be written to a text file
        filename(string): name of the file to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
