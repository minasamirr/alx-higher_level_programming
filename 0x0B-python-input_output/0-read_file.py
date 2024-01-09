#!/usr/bin/python3
"""
Module for reading a text file and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Function to read a text file and print its content to stdout.

    Parameters:
    - filename (str): The name of the file to be read.

    Returns:
    - None
    """
    # Open the file in read mode with UTF-8 encoding using 'with' statement
    with open(filename, encoding='utf-8') as file:
        # Read the content of the file
        content = file.read()

        # Print the content to stdout
        print(content, end="")
