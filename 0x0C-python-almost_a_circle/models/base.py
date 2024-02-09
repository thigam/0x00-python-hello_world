#!/usr/bin/python3
"""
Contains the definition for the class Base
"""


class Base:
    """
    Definition for the class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
