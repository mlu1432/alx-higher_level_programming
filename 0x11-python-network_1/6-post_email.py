#!/usr/bin/python3
"""
Make a POST request to the specified URL, including the email as parameter
"""
import requests
from sys import argv


def main(argv):
    """
    function sends a POST request to the specified URL,
    including the email as a parameter,
    and then displays the response body (decoded in UTF-8)
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    main(argv)
