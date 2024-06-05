#!/usr/bin/node
// Script prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');

// Get the API URL from the first command line argument
const apiUrl = process.argv[2];

// Make the GET request
request(apiUrl, function (error, response, body) {
         if (error) {
                 console.error('Error:', error);
                 return;
         }
        // Parse the response body as JSON
        const results = JSON.parse(body).results;

        // Count the number of films where the character appears
        const count = results.reduce((count, movie) => {
                return movie.characters.find((character) => character.endsWith('/18/'))
                ? count + 1
                : count;

                }, 0)
        // Print the count
        console.log(count);

});
