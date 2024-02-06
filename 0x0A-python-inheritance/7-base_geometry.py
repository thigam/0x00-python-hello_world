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

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            print("Reached")
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
