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
  if (error) {
    console.error(error);
    return;
  }

  // Check if request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: Status code ${response.statusCode}`);
    return;
  }

  // Parse the response body to JSON
  const movieData = JSON.parse(body);

  // Print the names of characters in the order they appear in the response
  movieData.characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Check if request was successful (status code 200)
      if (response.statusCode !== 200) {
        console.error(`Failed to retrieve data: Status code ${response.statusCode}`);
        return;
      }

      // Parse the response body to JSON
      const characterData = JSON.parse(body);

      // Print the name of the character
      console.log(characterData.name);
    });
  });
});
