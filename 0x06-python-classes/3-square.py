#!/usr/bin/python3
"""A class Square."""


class Square:
    """Represents a square with a default size."""

    def __init__(self, size=0):
        """Initializes a Sqaure.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not (int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
