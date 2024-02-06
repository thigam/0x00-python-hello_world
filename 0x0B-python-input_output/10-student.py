#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """
    Defines a class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        our_dict = {}
        for key, value in vars(self).items():
            if attrs is None:
                return vars(self)
            if key in attrs:
                our_dict[key] = value
        return our_dict
