#!/usr/bin/python3
"""
This module contains a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance
    of a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is exactly an instance
        otherwise False.
    """
    return (True if type(obj) == a_class else False)
