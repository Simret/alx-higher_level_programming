#!/usr/bin/python3
"""A function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """Function definition"""
    with open(filename, mode="r") as f:
        return json.load(f)
