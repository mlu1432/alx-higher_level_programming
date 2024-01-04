#!/usr/bin/node
// script display the status code of a GET request
// Print the error if one occurred
// Print the response status code if a response was received

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {console.log('code:', response && response.statusCode);
  }
});
