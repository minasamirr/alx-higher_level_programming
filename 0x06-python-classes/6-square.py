#!/usr/bin/python3
"""
Module: 6-square

Description:
    Contains the definition of the Square class.

Classes:
    Square
"""


class Square:
    """
    Square class represents a square.

    Attributes:
        __size (int): Private instance attribute representing the size of
                      the square.
        __position (tuple): Private instance attribute representing the
                            position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new Square
                                                  instance.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        position(self): Getter method to retrieve the position of the square.
        position(self, value): Setter method to set the position of the square.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character # and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): Optional size for the square (default is 0).
            position (tuple): Optional position for the square (default is
                              (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The position to set for the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # and position.

        If size is equal to 0, prints an empty line.
        Position is used by adding leading spaces and newlines when needed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
