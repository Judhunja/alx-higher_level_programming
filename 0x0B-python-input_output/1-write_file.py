#!/usr/bin/python3
""" This module contains a write_file function """


def write_file(filename="", text=""):
    """
    Returns the number of characters written to a file

    Args:
        filename(string): name of the file to write
        text(string): input to file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars_written = f.write(text)

    return chars_written
