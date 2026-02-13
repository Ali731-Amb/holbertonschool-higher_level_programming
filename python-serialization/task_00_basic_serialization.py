#!/usr/bin/python3
"""
This module provides utility
functions for serializing Python objects to
JSON files
and deserializing them back into Python
objects.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python object and save it to a JSON file.
    Args:
        data (any): The Python object to be
        serialized (must be JSON serializable).
        filename (str): The name or path of the
        file where the data will be saved.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Read a JSON file
    and deserialize its content into a Python object.
    Args:
        filename (str): The name or path of
        the JSON file to be read.
    Returns:
        any: The deserialized Python
        data (e.g., dict, list, str).
    """
    with open(filename, 'r') as f:
        return json.load(f)
