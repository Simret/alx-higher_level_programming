#!/usr/bin/python3
""" A module that creates a square"""


class Square:
    """A class that creates square"""
    def __init__(self, size=0):
        """Initialize fields"""
        self.__size = size

    @property
    def size(self):
        """Gettter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate square"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size != 0:
            for square in range(self.__size):
                print('#' * self.size)
            else:
                print("")
