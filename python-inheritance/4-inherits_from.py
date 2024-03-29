#!/usr/bin/python3
"""
This module defines the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True f the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
