#!/usr/bin/python3
"""This module will define the add_integer function"""


def add_integer(a, b=98):
    """Returns the sum of two integers
    args:
        a: an int or float value
        b: an int or float value
    rasies:
        TypeError: if either value is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
