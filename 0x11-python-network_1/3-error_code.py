#!/usr/bin/python3
"""
This script takes in a URL, sends a request to that URL, and displays the response body.
If an HTTP error occurs, it prints the error code.
If the connection fails, it prints an error message.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except urllib.error.URLError as e:
        print("Failed to reach the server.")
        print("Reason:", e.reason)
