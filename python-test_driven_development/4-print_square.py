#!/usr/bin/python3
"""This module will define the print_square function"""


def print_square(size):
    """Prints a square with the character #
    Args:
        size: size length of the square
    raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and less than zero
        ValueError: if size is less than 0
    """
    # check if size is an int
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
