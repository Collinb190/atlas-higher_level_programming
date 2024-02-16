#!/usr/bin/python3
"""This module will define the class_to_json function"""


def class_to_json(obj):
    """
    Returns the dictionary desctiption for JSON of an obj
    Args:
        obj: An instance of a class
    Returns:
        dict: A dictionary rep the serialized obj
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        return obj.__dict__.copy()
