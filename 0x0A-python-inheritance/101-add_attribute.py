#!/usr/bin/python3
"""A function that adds a new attribute to an object if it’s possible"""


def add_attribute(cla, attri, value):
    """A method that adds a new attribute to an object if it's possible"""
    if not(hasattr(cla, '__dict__')):
        raise TypeError("can't add new attribute")
    setattr(cla, attri, value)
