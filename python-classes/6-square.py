#!/usr/bin/python3
"""define a class Square."""


class Square:
    """represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """create a new square

        Args:
            size (int): the size of the square
            position (tuple): the position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get and set the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
