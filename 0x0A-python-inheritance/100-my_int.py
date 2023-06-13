#!/usr/bin/python3

class MyInt(int):
    """
    A class that represents an integer and inherits from int.
    The == and != operators are inverted.
    """
    def __eq__(self, other):
        """
        Overrides the default implementation of the ==.

        Returns:
            (bool): False if self and other are equal, True otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the default implementation of the !=.

        Returns:
            (bool): True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
