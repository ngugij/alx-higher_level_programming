#!/usr/bin/python3
"""MyInt module - inherits int"""


class MyInt(int):
    """inverts == and != in a class"""
    def __eq__(self, other):
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return True
