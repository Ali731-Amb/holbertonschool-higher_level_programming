#!/usr/bin/python3
import json
"""
    Writes an object to a text file using a JSON representation.
    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to write the JSON string to.
"""


def save_to_json_file(my_obj, filename):
    json_str = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_str)
