#!/usr/bin/python3
"""
This module contains a class square
"""


class Square:
    """
    This class initializes a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance variable with optional private
        instance attributes size and position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        A property that retrieves size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter that sets value of size after checking
        if it is valid
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Property that retrieves the value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter that sets the value of position after
        confirming that it is valid
        """
        if isinstance(value, tuple) and len(value) == 2\
                and all(isinstance(x, int) and x > 0 for x in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
