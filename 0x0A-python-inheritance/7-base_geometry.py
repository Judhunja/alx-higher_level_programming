#!/usr/bin/python3
""" This module contains a BaseGeometry class """


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
