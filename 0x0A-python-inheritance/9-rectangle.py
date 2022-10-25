#!/usr/bin/python3
"""Rectangle module - inherits
    BaseGeometry class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class inheritance"""
    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """returns area of a triangle"""
        return self.__width * self.__height

    def __str__(self):
        """return string repr of Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
