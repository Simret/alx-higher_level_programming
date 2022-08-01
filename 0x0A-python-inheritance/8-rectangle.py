#!/usr/bin/python3
"""A module that contains a class with public instance and private getters/setters"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with private height and width"""
    def __init__(self, width, height):
        """Initialization of class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
