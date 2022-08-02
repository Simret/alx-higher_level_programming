#!/usr/bin/python3
"""A module that contains a class with public instance and private getters/setters"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class with private height and width"""
    
    def __init__(self, width, height):
        """Initialization of class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height
