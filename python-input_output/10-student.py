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

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of a Student instance.
        Args:
            attrs (list): A list of strings.
        Returns:
            dict: A dictionary rep the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        return {
            attr: getattr(self, attr, None)
            for attr in attrs
            if hasattr(self, attr)
        }
