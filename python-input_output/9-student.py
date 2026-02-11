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

    def to_json(self):
        """
        Returns a dictionary representation
        of the Student instance suitable
        for JSON serialization.
        Returns:
            dict: A dictionary containing
            the student's attributes.
        """
        def serialize(valeur):
            if isinstance(valeur, (int, bool, str)) or valeur is None:
                return valeur
            elif isinstance(valeur, list):
                return [serialize(item) for item in valeur]
            elif isinstance(valeur, dict):
                new_dict = {}
                for key, val in valeur.items():
                    new_dict[key] = serialize(val)
                return new_dict
            elif hasattr(valeur, "__dict__"):
                return serialize(valeur.__dict__)
        return serialize(self)
