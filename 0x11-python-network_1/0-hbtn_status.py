#!/usr/bin/python3
"""
This script fetches the status from the ALX intranet URL using the urllib package and prints:
- The type of the response
- The raw byte content of the response
- The content decoded to UTF-8
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
