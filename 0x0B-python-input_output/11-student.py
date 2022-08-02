#!/usr/bin/python3
"""A module that contains a student class that defines a student"""


class Student:
    """A claass that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Arguments: first_name, last_name of the student, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representation of a Student instance"""
        new dict = {}
        if type(attrs) is list:
            if all(type(i) is str for i in attrs):
                for i in attrs:
                    if hasattr(self, i):
                        new_dict[i] = getattr(self, i)
                return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes"""
        for i in json:
            self.__dict__[i] = json[i]
