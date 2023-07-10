#!/usr/bin/python3
""" This module contains is_same_class function """


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the
    specified class

    Args:
        obj(object): object to be checked
        a_class(Class): class containing instance variables

    Returns:
        True if the object is an instance of the specified
        class, otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
