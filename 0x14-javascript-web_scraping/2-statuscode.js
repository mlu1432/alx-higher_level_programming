#!/usr/bin/node
// Script displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
        if (err) {
                console.error('error:', err);
                } else {
                console.log('code:', response && response.statusCode);
                }
});
