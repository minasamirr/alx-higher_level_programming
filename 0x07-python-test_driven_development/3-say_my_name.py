#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints the message: "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Walter", "White")
        My name is Walter White

        >>> say_my_name("Bob")
        My name is Bob

        >>> say_my_name(12, "White")
        Traceback (most recent call last):
          ...
        TypeError: first_name must be a string or last_name must be a string
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
