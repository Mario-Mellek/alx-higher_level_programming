#!/usr/bin/python3
"""
This module defines the MyList
class that inherits from list.
"""


class MyList(list):
    """
    A subclass of list
    provides a method to print a sorted version of the list.
    """
    def print_sorted(self):
        """
        prints ascending sort
        A sorted version of the list
        """
        print(sorted(self))
