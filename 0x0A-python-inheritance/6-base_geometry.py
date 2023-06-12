#!/usr/bin/python3
"""
This module contains a BaseGeometry class
Public instance method:area method that raises an exception.
"""


class BaseGeometry():
    """
    A class that represents the base geometry.
    """
    def area(self):
        """
        Raises an exception-> area method is not implemented.

        Raises:
            Exception: method is not implemented.
        """
        raise Exception("{}() is not implemented"
                        .format(self.area.__name__))
