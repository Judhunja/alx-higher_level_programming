#!/usr/bin/python3
""" This module contains a Rectangle class """


class Rectangle:
    """ Defines a rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes private instance attributes width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for _ in range(self.__height):
            rect += str(self.print_symbol) * self.__width + "\n"
        return rect.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
