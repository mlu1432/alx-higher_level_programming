#!/bin/bash
# script sends a request to a server endpoint that triggers a specific response

# Make a request with curl, including any necessary headers or other options
curl -sLX PUT "http://0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98" -H "You got me!"

