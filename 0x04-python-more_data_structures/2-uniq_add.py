#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_set = set()

    # Iterate through the elements of the input list
    for element in my_list:
        # Add the element to the set to ensure uniqueness
        unique_set.add(element)

    # Sum up the unique integers in the set and return the result
    result = sum(unique_set)
    return result
