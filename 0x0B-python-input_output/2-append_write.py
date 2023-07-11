#!/usr/bin/python3
""" This module contains append_write function """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a file

    Args:
        filename(string): name of the file
        text(string): string to append at the end of the file

    Returns:
        numbers of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        chars_appended = f.write(text)

    return chars_appended
