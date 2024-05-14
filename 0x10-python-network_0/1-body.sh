#!/bin/bash
# Sends a GET request to a URL passed as an argument
# and displays the body of a 200 status code response.
curl -Lsf "$1"

