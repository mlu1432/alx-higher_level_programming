#!/usr/bin/node
// Script prints all characters of a specified Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the GET request to fetch movie data
request(apiUrl, function (error, response, body) {
        if (error) {
                console.error('Error:', error);
                return;
        }

        if (response.statusCode !== 200) {
                console.error('Failed to fetch movie data. Status code:', response.statusCode);
                return;
        }

        // Parse the response body as JSON
        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        // Fetch and print character names
        characterUrls.forEach(characterUrl => {
                request(characterUrl, function (charError, charResponse, charBody) {
                        if (charError) {
                                console.error('Error fetching character:', charError);
                                return;
                        }

                        if (charResponse.statusCode !== 200) {
                                console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
                                return;
                        }

                        const characterData = JSON.parse(charBody);
                        console.log(characterData.name);
                });
        });
});
