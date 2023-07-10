#!/usr/bin/python3
""" This module contains a function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance of a class or is an
    instance of a baseclass of that class

    Args:
        obj(object): object to be checked
        a_class(Class): class

    Returns:
        True if the object is an instance of the class or its
        subclasses, else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
