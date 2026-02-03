#!/usr/bin/python3
"""
Module task_00_abc
This module defines an abstract class
hierarchy for animals with an abstract sound method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    Subclasses must implement the sound method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to return the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Class representing a cat.
    """
    def sound(self):
        return "Meow"
