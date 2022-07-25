#!/usr/bin/python3
"""A module that defines a rectangle class"""


class Rectangle:
    """A class has two attributes
    width
    height
    property and setter function definitions
    """

    def __init__(self, width=0, height=0):
        """A method that instantializes width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Setter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter validation if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter validation if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A method that returns area of a rectangle using given width and height"""
        return (self.width * self.height)

    def perimeter(self):
        """A method that returns perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)
