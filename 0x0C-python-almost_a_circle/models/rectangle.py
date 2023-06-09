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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validator(name, value):
        """Validate a value and raise appropriate errors.

        Args:
            name (str): name of the attribute being validated.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def coordinatesValidator(name, value):
        """Validate a coordinate value and raise appropriate errors.

        Args:
            name (str): name of the attribute being validated.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

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
        self.validator("width", value)
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
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle.

        Args:
            value (int): new x-coordinate of the rectangle.
        """
        self.coordinatesValidator("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle.

        Args:
            value (int): new y-coordinate of the rectangle.
        """
        self.coordinatesValidator("y", value)
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle.

         Returns:
             int: area of the rectangle.
         """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        The rectangle is printed with the width and height specified by the
        width and height attributes
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            for j in range(self.width - 1):
                print("#", end='')
            print("#")

    def __str__(self):
        """
        Returns a string representation of the instance

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.

        Args:
            *args: A variable-length list of arguments for
            updating the attributes.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)
        if not args:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance.

        Returns:
            dict: The dictionary representation of a Rectangle instance.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
