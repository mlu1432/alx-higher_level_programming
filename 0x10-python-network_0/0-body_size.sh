#!/bin/bash
# Takes in a URL, sends a request to that URL,
# and displays the size of the body of the response in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'



