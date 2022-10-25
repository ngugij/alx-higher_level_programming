#!/usr/bin/python3
"""Lookup function"""


def lookup(obj):
    """returns the list of available
    attributes and methods of an object"""
    return [method for method in dir(obj)]
