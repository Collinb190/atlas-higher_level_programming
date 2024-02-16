#!/usr/bin/python3
"""
This defines the write_file function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.

    Args:
        filename (str): The text file to act on.
        text (str): The string to be written into the file.
    Returns:
        numChars (int): The number of chars written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        numChars = file.write(text)
    return numChars
