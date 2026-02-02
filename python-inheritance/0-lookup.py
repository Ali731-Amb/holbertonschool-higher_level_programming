#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes and methods.
    """

def lookup(obj):
    return dir(obj)
