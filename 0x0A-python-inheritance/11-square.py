#!/usr/bin/python3
"""Square module - inherits
    Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class inheritance"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """string repr of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
