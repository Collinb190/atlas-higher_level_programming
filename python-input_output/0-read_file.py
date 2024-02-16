#!/usr/bin/python3
"""Module that defines the read_file function"""


def read_file(filename=""):
    """
    Read and print the content of text file
    Args:
        filename (str): The name of the file to act on
    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
