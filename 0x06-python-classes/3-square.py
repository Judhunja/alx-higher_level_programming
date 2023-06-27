#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """
    This class represents a square
    """
    def __init__(self, size=0):
        """
        initializes a square class with a size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
