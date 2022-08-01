#!/usr/bin/python3
"""A function that checks if object is instance of inherited class"""


def inherits_from(obj, a_class):
    """A method that checks if object is instance of a_class"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
