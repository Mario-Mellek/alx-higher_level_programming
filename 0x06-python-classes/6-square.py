#!/usr/bin/python3
"""A class Square."""


class Square:
    """Represents a square with a default size."""

    def __init__(self, size=0,  position=(0, 0)):
        """Initializes a Sqaure.

        Args:
            size (int): The size of the new square.
            position (tuple): The (x, y) coordinates.
        """
        if type(size) is not (int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not (tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not (int) or type(position[1]) is not (int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            The size of the square as an integer.
        """
        return self.__size

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if type(value) is not (int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        return self.__size

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (int): The new position of the square.
        """
        if type(value) is not (tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not (int) or type(value[1]) is not (int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints the square to stdout using the '#' character.
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def area(self):
        """
        calculates the area of the square.

        Returns:
            The area of the square as an integer.
        """
        return self.__size ** 2
