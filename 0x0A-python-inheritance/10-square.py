#!/usr/bin/python3
"""
This module contains a Square class that inherits from Rectangle.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class that represents a square and inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
