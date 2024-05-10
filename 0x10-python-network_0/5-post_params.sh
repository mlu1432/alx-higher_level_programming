#!/bin/bash
# This script sends a POST request to the given URL with specified form data
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
