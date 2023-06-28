#!/usr/bin/python3
"""
This module contains a class Square
"""


class Square:
    """
    A class that represents an square
    """

    def __init__(self, size=0):
        """
        initializes an instance variable with an optional
        attribute size
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
        sets a value to size after checking if it is valid i.e
        an integer and it is more than zero
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

    def my_print(self):
        """
        prints in stdout the square with the character '#'
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
