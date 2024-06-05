#!/usr/bin/node
// Script gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the GET request
request(url, function (error, response, body) {
        if (error) {
                console.error('Error:', error);
                return;

        }

        // Write the response body to the file
        fs.writeFile(filePath, body, 'utf8', function (err) {
                if (err) {
                        console.error('Error:', err);
                }
        });
});
