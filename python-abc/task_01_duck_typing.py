#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class representing a geometric shape.
    Must implement area and perimeter methods.
    """
    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Represents a circle with a given radius.
    """
    def __init__(self, radius=0):
        """
        Initializes a circle with the given radius.
        Args:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        Returns:
        float: Area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        Returns:
        float: Perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle with a width and a height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.
        Args:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        Returns:
        float: Area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        Returns:
        float: Perimeter of the rectangle.
        """
        return ((self.width + self.height) * 2)


def shape_info(shape):
    """Print the area and perimeter of a shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
