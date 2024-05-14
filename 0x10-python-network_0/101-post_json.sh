#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response.

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url=$1
filename=$2

# Check if the file exists
if ! [ -f "$filename" ]; then
    echo "Error: File does not exist"
    exit 1
fi

# Use curl to send a POST request with the JSON file content
response=$(curl -s -H "Content-Type: application/json" -d @"$filename" "$url")
echo $response
