#!/bin/bash
# This script accepts a URL as input, issues a request to that URL,
# and outputs the size of the response body.
curl -s "$1" -o /dev/null -w '%{size_download}\n'


