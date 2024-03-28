#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        headers = response.info()
        request_id = headers.get('X-Request-Id')
        print(request_id)
