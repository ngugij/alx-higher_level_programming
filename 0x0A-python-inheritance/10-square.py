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
