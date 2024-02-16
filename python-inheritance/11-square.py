#!/usr/bin/python3
"""This module defines the Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class reps a square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance
        Args:
            size: The size of the Sqaure
        """
        super().__init__(size, size)

    def __str__(self):
        """Returns a string rep of the Square"""
        return "[Square] {}/{}".format(self.width(), self.height())
