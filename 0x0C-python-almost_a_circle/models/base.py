#!/usr/bin/python3
"""
This module conatins a Base class definition
"""
import json


class Base:
    """Base class

    Attributes:
        __nb_objects (int): private class attribute:
            keeps track of the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method
        Base class constructor

        Args:
            id (int): id to assign to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        name = cls.__name__ + ".json"
        list_dicts = [o.to_dictionary() for o in list_objs]\
            if list_objs else []
        with open(name, 'w') as myFile:
            myFile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries
        represented by a JSON string.

        Args:
            json_string (str): A JSON string
            representing a list of dictionaries.

        Returns:
            list: The list of dictionaries
            represented by json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class
        with all attributes set.

        Args:
            **dictionary: A dictionary containing
                key-value pairs of attributes to set.

        Returns:
            An instance of the class with all
            attributes set according to the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file.

        Returns:
            A list of instances of the class.
            If the file doesn't exist, returns an empty list.
        """
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as myFile:
                data = myFile.read()
                dictionaries = cls.from_json_string(data)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []
