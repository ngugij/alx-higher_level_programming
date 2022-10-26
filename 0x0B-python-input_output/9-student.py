#!/usr/bin/python3
"""Student module"""


class Student:
    """creates a dictionary
        description of student"""

    def __init__(self, first_name, last_name, age):
        """initialize student"""
        self.first_name = first_name
        self.lst_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation"""
        return self.__dict__
