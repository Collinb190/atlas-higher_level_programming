#!/usr/bin/python3
"""This module will define the load_from _Json_file function"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    Args:
        filename (str): the name of the JSON file
    Returns:
        object: The python data structure rep b the JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
