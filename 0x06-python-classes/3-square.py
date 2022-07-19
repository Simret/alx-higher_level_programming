#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """everything is fine"""
            self.__size = size

    def area(self):
        return self.__size ** 2
