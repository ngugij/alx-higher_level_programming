#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """reads a text file (UTF8)
        and prints it to stdout"""
    if filename:
        with open(filename, mode="r", encoding='utf-8') as file:
            print(file.read(), end="")
