#!/usr/bin/python3
"""This module will define the to_json_string"""
import json


def to_json_string(my_obj):
    """
    This function will return the JSON rep of an object
    Args:
        my_obj: The object to be converted to JSON
    Returns:
        J (str): The JSON rep of the object
    """
    return json.dumps(my_obj)
