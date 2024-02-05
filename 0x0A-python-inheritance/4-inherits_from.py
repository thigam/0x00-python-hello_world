#!/usr/bin/python3
"""
Contains a function that only returns true if object is part of a class that directly inherited from inputted class
"""
def inherits_from(obj, a_class):
    """
    Checks whether it's part of a class that inherited directly from specified class
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
