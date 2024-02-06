#!/usr/bin/python3
"""
Contains a function that returns the dictionary description
with simple data structure for JSON serialization
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object
    Args:
        obj : the object
    Returns: It's dictionary description
    """
    return vars(obj)
