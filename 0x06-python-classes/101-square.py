#!/usr/bin/python3
"""Class defining a square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Args:
            size (int): size of a square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")

    def __str__(self):
        """Define the string representation of a square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
