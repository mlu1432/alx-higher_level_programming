#!/bin/bash
# This script accepts a URL as input, issues a request to that URL,
# and outputs the size of the response body.
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2


