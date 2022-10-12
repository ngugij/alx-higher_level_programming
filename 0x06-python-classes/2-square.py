#!/usr/bin/python3
"""Class defining a square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Initializes square

        Args:
            size (int): size of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
