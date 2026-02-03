#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional sorting
    functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
