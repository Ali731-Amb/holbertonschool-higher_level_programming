#!/usr/bin/python3
"""
Module for the Student class and
serialization to JSON.
This module defines a Student class and
provides a method to serialize its
attributes to a JSON-compatible dictionary.
"""


class Student:
    """
    Represents a student with first name,
    last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.
        If 'attrs' is a list of strings, only those attributes are included.
        Otherwise, all attributes are included.
        """
        data = self.__dict__
        if type(attrs) is list:
            return {
                    key: value for key,
                    value in data.items() if key in attrs
                    }
        else:
            return data
