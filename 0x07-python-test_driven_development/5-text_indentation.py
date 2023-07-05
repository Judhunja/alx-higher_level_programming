#!/usr/bin/python3
"""
this module contains a text_indentation function
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters:
    '.', '?' and ':'

    Args:
        text(str) : text to print out
        with new lines after the specified characters

    Raises:
        TypeError: if text isn't a string

    Returns:
        nothing
    """
    if text is None or text == "":
        raise TypeError("text must be a string")

    if type(text) != str:
        raise TypeError("text must be a string")

    first_line_char = False
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char, end='')
            print("\n")
            first_line_char = True
        else:
            if first_line_char and char.isspace():
                continue
            print(char, end='')
            first_line_char = False
