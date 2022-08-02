#!/usr/bin/python3
"""A function that returns dictionary description for JSON serialization"""


def class_to_json(obj):
    """Return dictionary"""
    return obj.__dict__
