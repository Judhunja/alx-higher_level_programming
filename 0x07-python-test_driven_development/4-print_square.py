#!/usr/bin/python3
def print_square(size):
    """
    prints a square with the character #

    Args:
        size: size length of the square

    Raises:
        TypeError: if size if not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than zero

    Returns:
        nothing(success)
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")

    for x in range(size):
        print("#" * size)
