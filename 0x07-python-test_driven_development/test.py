"""
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

>>> matrix = []
>>> matrix_divided([matrix, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix = None
>>> matrix_divided([matrix, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/
floats

>>> matrix = [
    [1, 2, 3, 4],
    [1, 2, 3]
]
>>> matrix_divided(matrix, 3)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix = [
    [1, 2, 3],
    [1, 2, 3, 4]
]
>>> matrix_divided(matrix, 3)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, [goat, camel])
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, {"dog": "joe"})
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, None)
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, True)
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, (goat, camel))
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, "animal")
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, 0)
Traceback (most recent call last):
ZeroDivisionError: division by zero

