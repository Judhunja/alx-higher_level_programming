#!/usr/bin/python3
"""
this module contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides every element of a matrix by a given number

    Args:
        matrix (list of lists): matrix to be divided by div.
        div (int or float): number to divide matrix by.

    Returns:
        list of lists: new matrix with all elements divided by div

    Raises:
        TypeError: if all the elements of the matrix are
        not integers or if the first list of the matrix is empty
        TypeError: if the rows of the matrix have different lengths
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    new_matrix = []
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    if matrix[0] == []:
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(matrix, list) or\
            any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    if any(not all(isinstance(elem, (int, float)) for elem in row)
           for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for sub_list in matrix:
        new_sub_list = [round(elem / div, 2) for elem in sub_list]
        new_matrix.append(new_sub_list)

    return new_matrix
