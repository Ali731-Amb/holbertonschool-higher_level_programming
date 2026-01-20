#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
        return (lenght, first_char)
