#!/usr/bin/python3
""" This module contains a pascal_triangle function """


def pascal_triangle(n):
    """
    Returns a list of lists of ints representing the Pascal's
    triangle of n

    Args:
        n(int): number representing pascal's triangle

    Returns:
        list of lists of ints, if n <= 0 returns an empty list
    """
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row_prev = triangle[i - 1]
                    val = row_prev[j - 1] + row_prev[j]
                    row.append(val)
            triangle.append(row)
        return triangle
