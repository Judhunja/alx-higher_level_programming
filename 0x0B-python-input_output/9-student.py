#!/usr/bin/python3
""" This module contains a class Student """


class Student:
    """ initializes a class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dict representation of Student instance that can
        be serializad to a JSON object
        """
        return vars(self)
