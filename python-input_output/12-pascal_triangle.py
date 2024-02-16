#!/usr/bin/python3
"""This module defines a function pascal_triangle."""


def pascal_triangle(n):
    """
    Generates pascals triangle up to the specified level
    Args:
        n (int): The number of levels to generate.
    Returns:
        list: A list of lists rep pascals triangle
    """
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        row = (
            [1] +
            [tri[i - 1][j - 1] + tri[i - 1][j] for j in range(1, i)] +
            [1]
        )
        tri.append(row)
    return tri


def print_triangle(tri):
    """
    Print the triangle
    Args:
        triangle (list): A list of lists rep pascals triangle
    """
    for row in tri:
        print("[{}]".format(",".join([str(x) for x in row])))
