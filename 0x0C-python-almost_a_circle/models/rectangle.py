#!/usr/bin/python3
""" This module contains a Rectangle class """
from models.base import Base


class Rectangle(Base):
    """Initializes a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the Rectangle with the character #"""
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """returns the string representation of Rectangle with x and y"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        variables = ["id", "width", "height", "x", "y"]

        for j, arg in enumerate(args):
            setattr(self, variables[j], arg)

        if not args:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dict representation of a Rectangle """
        attrs = {}
        prefixed_attrs = vars(self)

        for key, value in prefixed_attrs.items():
            if key.startswith("_Rectangle__"):
                attrs[key[len("_Rectangle__"):]] = value
            else:
                attrs[key] = value

        return attrs

    @property
    def width(self):
        """Retrieves the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of rectangle

        Args:
            value(int): value to set the width of Rectangle to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retreives the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of Rectangle

        Args:
            value(int): value to set the height of the
            Rectangle to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
