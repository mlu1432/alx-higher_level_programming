#!/usr/bin/python3
"""
This script takes a URL and an email address as command-line arguments,
sends a POST request to the URL
with email as parameter, and displays the body of the response decoded in utf-8
"""

from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
