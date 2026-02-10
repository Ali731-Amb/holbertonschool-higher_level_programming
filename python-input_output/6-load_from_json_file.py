#!/usr/bin/python3
import json
"""
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the JSON file to read from.
    Returns:
        object: The Python object created from the JSON file.
"""


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
