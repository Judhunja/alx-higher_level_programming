#!/usr/bin/python3
"""
This module contains save_to_json_file function,
load_from_json_file function and add_item function
"""
import json
import sys


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


def load_from_json_file(filename):
    """ Creates an object from a JSON file
    Args:
        filename(string): file containing JSON objects
    """
    with open(filename, encoding="utf-8") as json_f:
        return json.load(json_f)


def add_items(args):
    """ adds command line arguments to JSON file """
    all_args = []

    all_args = load_from_json_file("add_item.json")

    all_args.extend(sys.argv[1:])

    save_to_json_file(all_args, "add_item.json")

    return all_args
