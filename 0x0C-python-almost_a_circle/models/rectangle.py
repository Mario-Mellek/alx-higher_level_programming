#!/usr/bin/python3
"""
This module contains a class Rectangle definition
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        x (int): x-coordinate of the rectangle.
        y (int): y-coordinate of the rectangle.
        id (int): id of the rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle object.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): x-coordinate of the rectangle.
            y (int): y-coordinate of the rectangle.
            id (int): id of the rectangle object.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): new width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): new height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def width(self, value):
        """Set the x-coordinate of the rectangle.

        Args:
            value (int): new x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def width(self, value):
        """Set the y-coordinate of the rectangle.

        Args:
            value (int): new y-coordinate of the rectangle.
        """
        self.__y = value
