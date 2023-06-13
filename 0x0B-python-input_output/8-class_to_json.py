#!/usr/bin/python3
"""
This module contains a function that
returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object.
    """
    return (obj.__dict__)
