#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while count < x:
        try:
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end="")
                count += 1
            i += 1
        except IndexError:
            break
    print()
    return count
