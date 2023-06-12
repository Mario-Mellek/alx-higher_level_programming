#!/usr/bin/python3
"""
This module contains a BaseGeometry class
an area method that raises an exception
an integer_validator method that validates integers.
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

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value .
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
