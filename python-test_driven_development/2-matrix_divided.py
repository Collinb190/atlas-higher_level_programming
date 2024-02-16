#!/usr/bin/python3
"""This module will define the matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by divisor and returns a new matrix
    Args:
        matrix: A matrix whose elemets to divide
        div: divisor to be used in matrix
    Raises:
        TypeError: if the matrix is not of ints or floats
        ZeroDivisionError: if div is equal to 0
    """
    if not (all(isinstance(row, list) and
            all(isinstance(element, (int, float))
            for element in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMat = [[round(element / div, 2) for element in row] for row in matrix]
    return newMat
