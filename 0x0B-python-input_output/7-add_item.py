#!/usr/bin/python3
"""
This module contains a function
that adds all arguments to a Python list,
and then save them to a file:
"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def addItem():
    """Adds all command-line arguments to a Python list and
    saves the list to a file in JSON format.

    The list is saved as a JSON representation in a file named add_item.json.
    If the file doesn't exist, it is created.
    """
    myFile = 'add_item.json'

    try:
        aList = load_from_json_file(myFile)
    except FileNotFoundError:
        aList = []

    aList.extend(argv[1:])
    save_to_json_file(aList, myFile)


addItem()
