#!/usr/bin/python3
"""Class defining a square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Initializes square
        Args:
            size (int): size of a square
        """
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
