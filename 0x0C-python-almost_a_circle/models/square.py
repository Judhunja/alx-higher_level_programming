#!/usr/bin/python3
""" This module contains a class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializes a rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes value of width and height to size """
        super().__init__(size, size, x, y, id)

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
        variables = ["id", "width", "height", "x", "y"]
        if len(args) == 5:
            for j, arg in enumerate(args):
                setattr(self, variables[j], arg)
        else:
            for j, arg in enumerate(args):
                if j == 0:
                    self.id = arg
                elif j == 1:
                    self.width = arg
                    self.height = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg

        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dict representation of a Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ Overrides the Rectangle __str__ method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
