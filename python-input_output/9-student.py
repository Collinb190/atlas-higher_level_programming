#!/usr/bin/python3
"""This module will define a class Student."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The age of the student.
        """
        self.first_name = str(first_name) if first_name else ""
        self.last_name = str(last_name) if last_name else ""
        self.age = int(age)

    def to_json(self):
        """
        Gets a dictionary representation of a Student instance.
        """
        return self.__dict__
