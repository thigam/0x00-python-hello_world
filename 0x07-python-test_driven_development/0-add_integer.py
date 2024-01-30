#!/usr/bin/python3
"""
Module containing a function that adds 2 integers
"""
def add_integer(a, b=98):
    """
    Adds 2 integers
    Args:
        a (int): First integer
        b (int): Second integer
    Return:
        Sum (int)
    """
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
