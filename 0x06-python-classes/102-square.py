#!/usr/bin/python3
"""
Module: 102-square

Description:
    Contains the definition of the Square class.

Classes:
    Square
"""


class Square:
    """
    Square class represents a square.

    Attributes:
        __size (float or int): Private instance attribute representing the
                               size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates and returns the area of the square.
        __eq__(self, other): Equality comparison for squares based on area.
        __ne__(self, other): Inequality comparison for squares based on area.
        __lt__(self, other): Less than comparison for squares based on area.
        __le__(self, other): Less than or equal to comparison for squares
        based on area.
        __gt__(self, other): Greater than comparison for squares based on area.
        __ge__(self, other): Greater than or equal to comparison for squares
        based on area.

    Raises:
        TypeError: If size is not a number (float or integer).
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int): Optional size for the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size to set for the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if area is less than or equal to the other,
            False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison for squares based on area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if area is greater than or equal to the other,
            False otherwise.
        """
        return self.area() >= other.area()
