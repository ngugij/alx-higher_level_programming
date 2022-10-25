#!/usr/bin/python3
"""add_attribute module"""


class add_attribute(obj, attr, value):
    """adds a new attribute to an object
        if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
