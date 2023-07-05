#!/usr/bin/python3
"""
this module contains add_integer function
it takes two numbers, casts them into ints and then returns
the result of their addition
"""


def add_integer(a, b=98):
    """
    adds two integers

    parameters:
    a (int)
    b (int)

    returns: result of addition
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        int_a = round(a)
        int_b = round(b)
    return int_a + int_b
