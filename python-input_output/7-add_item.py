#!/usr/bin/python3


"""
Module for adding command line
arguments to a JSON file list.
This script loads a list from a
JSON file, adds command line arguments to it,
and saves the updated list back to the file.
"""


import sys


def main():
    """
    Main function to add command line
    arguments to a list stored in a JSON file.

    Loads the list from 'add_item.json'
    if it exists, appends command line arguments,
    and saves the updated list back to the file.
    """


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
if __name__ == "__main__":
    main()
    _argv = sys.argv[1:]
    try:
        ma_liste = load_from_json_file("add_item.json")
    except FileNotFoundError:
        ma_liste = []
    ma_liste.extend(_argv)
    save_to_json_file(ma_liste, "add_item.json")
