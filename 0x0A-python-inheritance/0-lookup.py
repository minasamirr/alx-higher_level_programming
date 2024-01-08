#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object for which attributes and methods are to be looked up.

    Returns:
    - A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
