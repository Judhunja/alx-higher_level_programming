#!/usr/bin/python3
""" This module contains inherits_from function """


def inherits_from(obj, a_class):
    """
    Checks of an object is an instance of a class that
    inherited from the specified class

    Args:
        obj(object): object to be checked
        a_class: class which inherits from other classes

    Returns:
        True if the object is an instance of a class that
        inherited from the specified class, otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
