#!/usr/bin/python3
"""
A function that adds 2 integers

returns the sum of a & b
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add. Defaults to 98.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
