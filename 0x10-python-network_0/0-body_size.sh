#!/bin/bash
# Send a request to the provided URL and display the size of the response body in bytes
curl -s "$1" | wc -c
