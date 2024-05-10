#!/bin/bash
# This script sends a JSON POST request to the specified URL and displays the response body.

# Check if file exists
if [ ! -f "$2" ]; then
    echo "File not found!"
    exit 1
fi

# Send a POST request with the JSON file content
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
