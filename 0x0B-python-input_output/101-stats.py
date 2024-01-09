#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """
    Print statistics based on the accumulated data.

    Parameters:
    - total_size (int): Total file size.
    - status_codes (dict): Dictionary containing counts for each status code.

    Returns:
    - None
    """
    print("File size: {:d}".format(total_size))

    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))


def parse_line(line, total_size, status_codes):
    """
    Parse a line and update total size and status code counts.

    Parameters:
    - line (str): Input line to be parsed.
    - total_size (int): Current total file size.
    - status_codes (dict): Dictionary containing counts for each status code.

    Returns:
    - None
    """
    elements = line.split()
    if len(elements) >= 7:
        status_code = elements[-2]
        size = int(elements[-1])
        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    return total_size


if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size = parse_line(line, total_size, status_codes)

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
