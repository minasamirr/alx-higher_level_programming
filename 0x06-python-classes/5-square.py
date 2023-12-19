#!/usr/bin/python3
"""
Module: 5-square

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
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character #.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): Optional size for the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
