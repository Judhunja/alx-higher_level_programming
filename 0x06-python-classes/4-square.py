#!/usr/bin/bash
"""
This module contains a class Square
"""


class Square:
    """
    Initializes a square
    """
    def __init__(self, size=0):
        """
        Initializes an instance variable with an optional attribute size
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieves a private instance attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets a private instance attribute size after making
        sure that it has received a valid value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
