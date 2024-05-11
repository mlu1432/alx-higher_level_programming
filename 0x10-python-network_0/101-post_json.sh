#!/bin/bash
# This script sends a JSON POST request to the specified URL and displays the response body.

# Check if the file exists and if it's a readable file
if [ ! -f "$2" ] || [ ! -r "$2" ]; then
    echo "Error: File does not exist or cannot be read"
    exit 1
fi

# Send a POST request with the JSON file content
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
