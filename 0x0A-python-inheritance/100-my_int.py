#!/usr/bin/python3
"""A module that contains a class MyInt that inherits from int"""


class Int(int):
    """A class MyInt that inherits from int"""

    def __eq__(self, num):
        """Equal"""
        if (self.real == num):
            return False
        return True

    def __ne__(self, num):
        "No equal"
        if(self.real != num):
            return False
        return True
