#!/usr/bin/python3
"""A Function to divide all elements of a matrix
Prototype: def matrix_divided(matrix, div)
matrix must be a list of lists of integers or floats
    -TypeError ("matrix must be a matrix (list of lists)
    of integers/floats")
Each row of the matrix must be of the same size
    -TypeError ("Each row of the matrix must
    have the same size")
div must be a number (integer or float),
    -TypeError ("div must be a number")
div can’t be equal to 0
    -ZeroDivisionError ("division by zero")
All elements of the matrix should be divided by div
rounded to 2 decimal places
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """function to divide all elements of a matrix
    Raises:
    -TypeError ("matrix must be a matrix (list of lists)
    of integers/floats")
    -TypeError ("Each row of the matrix must
    have the same size")
    -TypeError ("div must be a number")
    -ZeroDivisionError ("division by zero")
    Return: new matrix
    """
    msg_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg_error)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(msg_error)

    first_row = len(matrix[0])
    for row in matrix:
        if first_row != len(row):
            raise TypeError('Each row of the matrix must have the same size')

    return [[round(i / div, 2) for i in row] for row in matrix]
