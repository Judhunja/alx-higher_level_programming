#!/usr/bin/python3
""" This module contains a Rectangle class """


class Rectangle:
    """ defines a Rectangle class """
    def __init__(self, width=0, height=0):
        """
        Initializes insatnce attributes width and class which are optional
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width if the given conditions are met """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height if the given conditions are met """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
