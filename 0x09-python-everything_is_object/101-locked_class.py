#!/usr/bin/python3
"""
A module containing a locked class
"""


class LockedClassParent:
    """Parent class with attribute restriciton"""
    __slots__ = ('first_name')
class LockedClass(LockedClassParent):
    """
    Empty class
    """
    __slots__ = ()
