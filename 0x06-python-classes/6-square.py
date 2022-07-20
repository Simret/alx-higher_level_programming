#!/usr/bin/python3
"""A module that defines a class Square"""


class Square:
    """A class square"""
    def __init__(self, size=0, position=(0, 0)):
    """Initialize a new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set size of the square""" 
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value)
        """Set position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
        self.__position = value

    def area(self):
        """Calculate the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.size != 0:
            for square_p in range(0, self.__position[1]):
                print('')
            for square_s in range(0, self.size):
                print('{}{}'.format(' ' * self.__position[0], '#'*self.__size))
        else:
            print('')
