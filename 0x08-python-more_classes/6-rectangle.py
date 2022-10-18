#!/usr/bin/python3
"""Class"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints the rectangle with character #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle
            to be able to recreate a new instance"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
