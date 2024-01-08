#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check for inheritance.

    Returns:
    - True if the object is an instance of a class that inherited from a_class,
      otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
