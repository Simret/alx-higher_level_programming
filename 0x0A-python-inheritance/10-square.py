#!/usr/bin/python3
"""A module that contains a class with public instance"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from rectangle"""
    
    def __init__(self, size):
        """Initalization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
