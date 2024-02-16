#!/usr/bin/python3
"""This module defines the append_write function."""


def append_write(filename="", text=""):
    """
    This appends a string onto a text file.
    Args:
        filename (str): The file to act on.
        text (str): The string to append.
    Returns:
        numChar (int): The number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        numChar = file.write(text)
    return numChar
