#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the,
X-Request-Id variable found in the response header.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
