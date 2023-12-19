#!/usr/bin/python3
"""
Module: 103-magic_class

Description:
    Contains the definition of the MagicClass class that performs
    the same functionality as the provided Python bytecode.

Classes:
    MagicClass
"""

import math


class MagicClass:
    """
    MagicClass class that performs the same functionality as
    the provided Python bytecode.

    Attributes:
        __radius (float): Private instance attribute representing the radius.

    Methods:
        __init__(self, radius=0): Initializes a new MagicClass instance.
        area(self): Calculates and returns the area of the MagicClass instance.
        circumference(self): Calculates and returns the circumference
                             of the MagicClass instance.

    Raises:
        TypeError: If radius is not a number (float or integer).
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (float or int): Optional radius for the MagicClass.

        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')

        self.__radius = float(radius)

    def area(self):
        """
        Calculates and returns the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass.
        """
        return 2 * math.pi * self.__radius
