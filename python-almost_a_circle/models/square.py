#!/usr/bin/python3
"""This module will define the Square class."""
from .rectangle import Rectangle


class Square(Rectangle):
    """This class will inherit from the Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Create an instance with these fields."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string rep of a square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary rep of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
