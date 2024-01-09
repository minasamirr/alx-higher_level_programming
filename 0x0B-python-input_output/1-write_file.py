#!/usr/bin/python3
"""
Module for writing a string to a text file and returning the number of
characters written.
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a text file and return the number of
    characters written.

    Parameters:
    - filename (str): The name of the file to be written.
    - text (str): The string to be written to the file.

    Returns:
    - int: The number of characters written to the file.
    """
    # Open the file in write mode with UTF-8 encoding using 'with' statement
    with open(filename, mode='w', encoding='utf-8') as file:
        # Write the text to the file
        nb_characters = file.write(text)

    # Return the number of characters written
    return nb_characters
