#!/usr/bin/python3
"""define a class Square."""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """create a new square

        Args:
            size (int): the size of the square

        """
        self.__size = size

    @property
    def size(self):
        """Get and set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.__size)
