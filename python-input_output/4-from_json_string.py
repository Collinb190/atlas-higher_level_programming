#!/usr/bin/python3
"""This module will define the from_json_string"""
import json


def from_json_string(my_str):
    """
    Returns a python data structure rep by JSON string
    Args:
        my_str (str): JSON string to be converted to python object
    Returns:
        object: The python data structure rep by JSON string
    """
    return json.loads(my_str)
