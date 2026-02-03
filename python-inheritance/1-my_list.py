#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print its elements
    in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        Assumes all elements in the list are of types that can be compared.
        """
        new_list = sorted(self)
        print(new_list)
