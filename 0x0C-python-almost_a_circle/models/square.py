#!/usr/bin/python3
"""
This module contains a class Rectangle definition
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
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

    @property
    def size(self):
        """
        Gets the size of the Square instance.

        Returns:
            int: The size of the Square instance.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets the size of the Square instance.

        Args:
            size (int): The new size of the Square instance.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.
        The order of the arguments in *args is important: id, size, x, y.

        Args:
            *args: A variable-length list of arguments
            **kwargs: A dictionary of keyword arguments
        """
        attrs = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attrs):
                if attrs[i] == "size":
                    self.width = arg
                    self.height = arg
                else:
                    setattr(self, attrs[i], arg)

        if not args:
            for key, value in kwargs.items():
                if key in attrs:
                    if key == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, key, value)
