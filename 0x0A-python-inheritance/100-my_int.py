#!/usr/bin/python3
""" This module contains MyInt class """


class MyInt(int):
    """
    Changes the behaviour of the equal to an not equal to
    operators
    """
    def __eq__(self, other):
        return self % 2 != other % 2

    def __ne__(self, other):
        return self % 2 == other % 2
