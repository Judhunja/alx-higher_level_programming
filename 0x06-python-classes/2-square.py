#!/usr/bin/python3
"""This module contains a class Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initializes an instance of the class Square with an
        optional argument size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
