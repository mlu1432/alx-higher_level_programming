#!/bin/bash
# This script takes a URL as an argument and,
# prints the size of the body of the response in bytes.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
body_size=$(curl -s -o /dev/null -w '%{size_download}' "$url")
echo $body_size
