#!/usr/bin/python3
"""This module will define the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name
    Args:
        first_name: The first name to be printed
        last_name: The last name to be printed
    Rasies:
        TypeError: If either arg is not a string
    """
    # check if args are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    fullName = first_name + " " + last_name
    print("My name is", fullName)
