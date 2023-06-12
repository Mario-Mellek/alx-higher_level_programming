#!/usr/bin/python3
"""
This module contains a function that checks
if an object is an instance of a
specified class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of
    a specified class or a subclass thereof.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class
        or a subclass; otherwise False.
    """
    return (True if isinstance(obj, a_class) else False)

