#!/usr/bin/python3

"""
BaseGeometry and Rectangle classes
"""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Public instance method that is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
