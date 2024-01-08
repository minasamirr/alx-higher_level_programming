#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A class representing MyInt that inherits from int.

    MyInt is a rebel. It has == and != operators inverted.

    Methods:
    - __eq__(self, other): Overrides the equality operator (==).
    - __ne__(self, other): Overrides the inequality operator (!=).
    """
    def __eq__(self, other):
        """
        Overrides the equality operator (==).

        Parameters:
        - other: The object to compare with.

        Returns:
        - True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=).

        Parameters:
        - other: The object to compare with.

        Returns:
        - True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
