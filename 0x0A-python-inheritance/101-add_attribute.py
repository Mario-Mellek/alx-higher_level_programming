#!/usr/bin/python3
"""
This module contains a function
that adds a new attribute to an object if it's possible
"""


def add_attribute(obj, attr, val):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the attribute to.
        attr (str): The name of the attribute to add.
        val (any): The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
