#!/usr/bin/python3
""" This module contains a Rectangle class """


class Rectangle:
    """ defines a Rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """ Retrieves the width """
    def width(self):
        return self.__width

    @width.setter
    """ sets the value of width if the given conditions are met """
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    """ retrieves the height """
    def height(self):
        return self.__height

    @height.setter
    """ sets the value of height if the given conditions are met """
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
