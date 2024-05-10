#!/bin/bash
# Sends a GET request to a URL passed as an argument
# and displays the body of a 200 status code response.
curl -s "$1" -o response.txt -w '%{http_code}' | grep -q "200" && cat response.txt && rm response.txt

