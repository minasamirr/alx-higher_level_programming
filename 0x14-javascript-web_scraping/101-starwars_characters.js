#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie-ID>');
  process.exit(1);
}

// Define the API endpoint URL for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
