#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    Parameters:
    - filename (str): The name of the file.
    - search_string (str): The specific string to search for in each line.
    - new_string (str): The line of text to be inserted after each line
    containing the search string.

    Returns:
    - None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
