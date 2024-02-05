#!/usr/bin/python3
"""
Contains a class that raises an exception
"""


class BaseGeometry:
    """
    Raise an exception when public instance method area is called
    """
    def area(self):
        raise Exception("area() is not implemented")
