#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, atr, value):
    """adds a new attribute to an object
        if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
