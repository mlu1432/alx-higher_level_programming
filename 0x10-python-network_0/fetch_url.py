#!/usr/bin/python3
"""
This module demonstrates making an HTTP request using the urllib package to a local server.
"""

import urllib.request

def fetch_url(url):
    """
    Fetches the content from the provided URL.
    
    Args:
        url (str): The URL to fetch the content from.
    
    Returns:
        str: The content of the URL.
    """
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

if __name__ == "__main__":
    url = "http://0.0.0.0:5000"
    content = fetch_url(url)
    print(content)
