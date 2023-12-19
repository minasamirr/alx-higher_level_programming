#!/usr/bin/python3
"""
Module: 1-square

Description:
    Contains the definition of the Square class.

Classes:
    Square
"""


class Square:
    """
    Square class represents a square.

    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size for the square.
        """
        self.__size = size
