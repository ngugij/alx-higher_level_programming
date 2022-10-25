#!/usr/bin/python3
"""MyList function that
inherits from list"""


class MyList(list):
    """list is inherited by MyList"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
