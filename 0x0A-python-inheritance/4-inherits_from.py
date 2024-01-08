#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Defines a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class; otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class to compare with.

    Returns:
    - True if obj is an instance of a class inherited from a_class;
    False otherwise.
    """
    return issubclass(type(obj), a_class)
