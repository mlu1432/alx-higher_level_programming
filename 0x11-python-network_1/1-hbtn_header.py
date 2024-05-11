#!/usr/bin/python3
"""
This script takes a URL as a command-line argument, sends a request to the URL, 
and displays the value of the 'X-Request-Id' header from the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req) as response:
            # Retrieve the value of the 'X-Request-Id' header
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
