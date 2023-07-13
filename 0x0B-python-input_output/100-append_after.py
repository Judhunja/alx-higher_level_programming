#!/usr/bin/python3
""" This module contains append_after function """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file after each line
    containing a specific string

    Args:
        filename(string): file to store the new string
        search_string(string): line of text after which to
        insert the new string
        new_string: string to insert
    """
    with open(filename, 'r', encoding="utf-8") as s_file:
        lines = s_file.readlines()

    with open(filename, 'w', encoding="utf-8") as s_file:
        for line in lines:
            s_file.write(line)
            if search_string in line:
                s_file.write(new_string)
