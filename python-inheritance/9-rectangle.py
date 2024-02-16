#!/usr/bin/python3
"""
This module will define the class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """
        Inititalizes a Rectangle instance.
        Args:
            width: The width of the Rectangle
            height: The height of the Rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string rep of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height
