#!/usr/bin/python3
"""
This module conatins a Base class definition
"""
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
