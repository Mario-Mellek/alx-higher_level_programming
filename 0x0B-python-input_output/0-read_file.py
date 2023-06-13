#!/usr/bin/python3
"""
This module contains a function that reads
a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints them to the console.

    Args:
        filename(str): : The name of the file to read.
    """
    with open(filename, encoding="utf-8") as myFile:
        text = myFile.read()
        print(text, end="")
