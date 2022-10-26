#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
        line containing a specific string"""
    text = ""
    with open(filename, mode="r", encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if line.find(serch_string) != -1:
            text = text + line + new_string
        else:
            text = text + line
    with open(filename, mode="w", encoding='utf-8') as file:
        file.write(text)
