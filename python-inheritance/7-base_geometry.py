#!/usr/bin/python3
"""
This module will define the class BaseGeometry.
"""


class BaseGeometry:
    """This class is the BaseGeometry class."""

    def area(self):
        """This method will print an exception message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method will validate the value.
        Raises: a TypeError exception if the value is not an integeger.
        Raises: a ValueError if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
