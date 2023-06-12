#!/usr/bin/python3
"""
This module contains a function that checks
if an object is an instance of a class that inherited
(directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited (directly or indirectly) from a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of a class
        that inherited (directly or indirectly);
        otherwise False.
    """
    return (True if issubclass(type(obj), a_class)
            and type(obj) != a_class else False)
