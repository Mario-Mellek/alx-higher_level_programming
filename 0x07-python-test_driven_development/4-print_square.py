#!/usr/bin/python3
"""
The module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    A function that prints a square represented with the character #.

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError:  size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
