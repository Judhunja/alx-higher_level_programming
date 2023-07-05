#!/usr/bin/python3
"""
This module contains a class LockedClass
"""


class LockedClass:
    """
    prevents a user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name
    """

    __slots__ = ("first_name")

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
