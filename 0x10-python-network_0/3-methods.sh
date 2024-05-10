#!/bin/bash
# program designed to input a web address and reveal all the
#HTTP methods supported by the corresponding server
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
