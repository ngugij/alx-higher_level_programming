#!/usr/bin/python3
"""Student module"""


class Student:
    """creates a dictionary
        description of student"""

    def __init__(self, first_name, last_name, age):
        """initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation"""
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for attr in attrs:
            try:
                n_dict[attr] = self.__dict__[attr]
            except Exception:
                pass
        return n_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception:
                pass
