#!/usr/bin/python3
"""
Module for appending a string to the end of a text file and returning
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Function to append a string to the end of a text file and return the
    number of characters added.

    Parameters:
    - filename (str): The name of the file to be appended.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added to the file.
    """
    # Open the file in append mode with UTF-8 encoding using 'with' statement
    with open(filename, mode='a', encoding='utf-8') as file:
        # Write the text to the end of the file
        nb_characters_added = file.write(text)

    # Return the number of characters added
    return nb_characters_added
