#!/usr/bin/python3
"""This module will define the save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON rep
    Args:
        my_obj: The object to be serialized to JSON
        filename (str): The name of the text file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
