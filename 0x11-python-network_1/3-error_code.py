#!/usr/bin/python3
"""
This script takes a URL as a command-line argument, sends a request to the URL,
 and displays the body of the response decoded in utf-8.
If an HTTP error occurs, it catches the exception and
 prints 'Error code:' followed by the HTTP status code.
"""

import urllib.request
from sys import argv

def main(argv):
    """
    Sends a GET request to the specified URL and
    prints the response content in UTF-8 encoding.
    Handles URLError exceptions specifically,
    printing the HTTP status code associated with the error.

    Args:
        argv (list): Command-line arguments
        where argv[1] is expected to be the URL to request.
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
