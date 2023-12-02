#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

def send_post_request(url, email_value):
    """Sends a POST request with the specified email to the    given URL.
    """

    data = urllib.parse.urlencode({'email': email_value})
    data = data.encode('utf-8')  # data should be bytes
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print("Your email is: {}".format(email_value))
        print(response.read().decode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email_value = sys.argv[2]
