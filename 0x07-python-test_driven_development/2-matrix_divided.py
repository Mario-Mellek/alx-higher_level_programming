#!/usr/bin/python3
"""
The module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The number to divide the elements by.

    Returns:
        list of lists: A new matrix where all elements are divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
        if each row of the matrix is not of the same size,
        or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(isinstance(value, (int, float)) for row in matrix
               for value in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    rowSize = len(matrix[0])
    if not all(len(row) == rowSize for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(value / div, 2) for value in row] for row in matrix]
    return result
