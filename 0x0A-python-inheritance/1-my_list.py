#!/usr/bin/python3
""" This module contains a class MyList """


class MyList(list):
    """
    a class inheriting from list
    """
    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
