#!/usr/bin/python3
"""
This module contains a function that
inserts a line of text to a file, after each line
containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename (str): The path to the file.
        search_string (str): The string to search for in the file.
        new_string (str): The string to insert into the file.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        text = myFile.readlines()

    with open(filename, mode="w", encoding="utf-8") as myFile:
        for line in text:
            myFile.write(line)
            if search_string in line:
                myFile.write(new_string)
