#!/usr/bin/python3
"""
This module contains a class Rectangle definition
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the Square instance.
            x (int): The x coordinate of the Square instance.
            y (int): The y coordinate of the Square instance.
            id (int): The id of the Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string representation of the Square instance.
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width
            )
