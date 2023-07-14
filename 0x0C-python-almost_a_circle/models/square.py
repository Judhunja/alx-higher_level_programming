#!/usr/bin/python3
""" This module contains a class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializes a rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes value of width and height to size """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        """Retrieves the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the value of width and height to be equal to size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ assigns arguments to attributes """
        for j, arg in enumerate(args):
            if j == 0:
                self.id = arg
            elif j == 1:
                self.size = arg
            elif j == 2:
                self.x = arg
            elif j == 3:
                self.y = arg

        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """ Overrides the Rectangle __str__ method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
