#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A class representing the base geometry.

    Methods:
    - area(self): Raises an Exception with the message
    "area() is not implemented".
    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
