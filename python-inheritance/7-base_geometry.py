#!/usr/bin/python3

"""
Add def integer_validator
"""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Public instance method that is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a integer"""
        if value is not isinstance(value, int):
            raise TypeError(f"{name}' must be a integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
