#!/usr/bin/python3
"""
This module contains a definition of a class Student
that has an init method and a to_json method
"""


class Student:
    """
    Defines a student.

    Public instance attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with the values from a dictionary.

    Args:
        json (dict): A dictionary where keys are
        attribute names and values are attribute values.
        """
        for key, val in json.items():
            setattr(self, key, val)
