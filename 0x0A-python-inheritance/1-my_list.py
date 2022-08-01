#!/usr/bin/python3
"""A module that contains a class which inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Print the list sorted ascending order"""
        print(sorted(list(self)))
