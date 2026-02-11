#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for ligne in f:
            print(ligne, end='')
