#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method.

    Methods:
    - print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Sorting the list in-place and printing the result.
        """
        sorted_list = sorted(self)
        print(sorted_list)
