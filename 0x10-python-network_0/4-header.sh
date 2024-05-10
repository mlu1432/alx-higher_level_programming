#!/bin/bash
# This script sends a GET request to the given URL with a custom header
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
