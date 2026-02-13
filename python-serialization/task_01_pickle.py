#!/usr/bin/python3


import pickle


class CustomObject():
    def __init__(self, name, age, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            "Name: {}\nAge: {}\nIs Student: {}".format(
                self.name, self.age, self.is_student)
        )

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, EOFError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, OSError, EOFError):
            return None
