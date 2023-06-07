#!/usr/bin/python3
"""
The module contains a function that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    A unction that prints My name is <first name> <last name>

    Args:
        first_name (str): first_name arg
        last_name (str): second_name arg

    Raises:
        TypeError: first and last names must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if len(last_name) > 0:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
