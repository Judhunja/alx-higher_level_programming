#!/usr/bin/python3
""" This module contains a BaseGeometry class and a class
    Rectangle that inherits from BaseGeometry and a class
    Square that inherits from Rectangle
"""


class BaseGeometry:
    """ Initializes a BseGeometry class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemeted")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Initializes a class Rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ str method that prints the width and height of the
        rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ initializes a class Square """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
