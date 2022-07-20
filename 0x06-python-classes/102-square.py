#!/usr/bin/python3
"""Module that compares squares"""


class Square:
    """Initialize fields"""
    def __init__(self, size=0):
        """Initialize size"""
        self.size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value)
        """Set size"""
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not Equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal"""
        return self.area() >= other.area() 
