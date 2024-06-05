#!/usr/bin/node
// Script reads and prints the title of a Star Wars movie based on the given movie ID

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (err, response, body) {
        if (err) {
                console.error('Error:', err);
                } else {
                const movie = JSON.parse(body);
                        console.log(movie.title);
                }
});
