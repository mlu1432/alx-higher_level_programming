#!/bin/bash
# This script sends a GET request with a custom header to a URL and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
