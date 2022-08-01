#!/usr/bin/python3
"""A function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """A method that returns the list of available attributes, methods and object"""
    return [method_name for method_name in dir(obj)]
