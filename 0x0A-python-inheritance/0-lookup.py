#!/usr/bin/python3
"""
This module contains a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    returns the list of available
    attributes and methods of an object

    Args:
        obj(object): The object to get the list
        of attributes and methods for.

    Returns:
        list: A list of strings representing the names of the available
        attributes and methods of the object.
    """
    return (dir(obj))
