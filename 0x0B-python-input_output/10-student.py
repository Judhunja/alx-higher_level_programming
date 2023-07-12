#!/usr/bin/python3
""" This module contains a Student class """


class Student:
    """ Initializes a Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dict representation of a Student instance,
        if attrs is a list of strings only attribute names
        contained in the list must be retrieved
        """
        if isinstance(attrs, list) and attrs is not None:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        else:
            return vars(self)
