#!/usr/bin/python3

"""A module that contains a class defining a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """A Method that initializes width and height fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
