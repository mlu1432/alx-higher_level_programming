#!/usr/bin/python3
"""
This script takes a URL as a command-line argument, sends a request to the URL
and displays the value of the 'X-Request-Id' header from the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
