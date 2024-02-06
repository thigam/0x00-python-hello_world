#!/usr/bin/python3
"""
Contains function that adds a new attribute to an object
"""


def add_attribute(self, name, attr):
    try:
        setattr(self, name, attr)
    except Exception:
        raise TypeError("Can't add new attribute")
