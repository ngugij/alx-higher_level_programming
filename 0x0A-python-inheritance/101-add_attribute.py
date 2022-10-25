#!/usr/bin/python3
"""add_attribute module"""


class add_attribute(obj, atr, value):
    """adds a new attribute to an object
        if it’s possible"""
    check = {int, str, float, list, dict, tuple, frozenset, type, object}

    if type(obj) in check:
        raise TypeError("can't add new attribute")
    obj.__setattr__(atr, value)
