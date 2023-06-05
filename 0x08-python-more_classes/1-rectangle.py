#!/usr/bin/python3
"""
Module defines a Rectangle class
"""


class Rectangle:
    """
    Class that represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Intializes a Rectangle object with width and height

        args:
            width (int): rectangle's width. default is 0
            height (int): rectangle's height. default is 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter that gets the width of the rectangle

        Returns: the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Getter that gets the height of the rectangle

        Returns: the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter that sets the width of the rectangle

        Args:
            value (int): the width of the rectangle

        Raises:
            TypeError: value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter that sets the height of the rectangle

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
