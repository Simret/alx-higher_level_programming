#!/usr/bin/python3
"""A module that contains a class defining a rectangle"""


class Rectangle:
    """A class that defines a rectangle with attributes and methods"""

    def __init__(self, width=0, height=0):
        """A method that initializes width and height fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A method that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """A method that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """A method that returns a printable rectangle"""
        rect = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                for j in range(self.width):
                    rect += "{}".format("#")
                if i < self.height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """A method that returns a string representation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """A method that deletes instance and print message"""
        print("Bye rectangle...")
