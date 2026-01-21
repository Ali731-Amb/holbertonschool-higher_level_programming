#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        b_dictionary[key] = new_value
    return b_dictionary
