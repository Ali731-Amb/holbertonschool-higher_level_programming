#!/usr/bin/python3
""" Module to convert a class instance into a JSON dictionary """


def class_to_json(obj):
    """Returns the dictionary description of an object"""
    return serialize(obj.__dict__)


def serialize(valeur):
    """Recursive function to transform the object into simple types"""
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
