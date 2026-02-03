#!/usr/bin/python3
"""
This module defines a BaseGeometry class and a subclass Rectangle.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height
