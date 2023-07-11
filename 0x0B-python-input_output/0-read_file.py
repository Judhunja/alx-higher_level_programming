#!/usr/bin/python3
""" This module contains a read_file function """


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Args:
        filename(string): name of the file to open and read
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
