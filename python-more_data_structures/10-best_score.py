#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or a_dictionary == {}:
        return None
    max_score = None
    best_key = None
    for key, value in a_dictionary.items():
        if max_score is None or max_score < value:
            max_score = value
            best_key = key
    return best_key
