#!/usr/bin/python3
"""
This module contains a function
that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object represented by
        the contents of the JSON file.
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
