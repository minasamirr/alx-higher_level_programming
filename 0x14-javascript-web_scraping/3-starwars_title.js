#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Define the API endpoint URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: Status code ${response.statusCode}`);
    return;
  }
  
  // Parse the response body to JSON
  const movieData = JSON.parse(body);
  
  // Print the title of the movie
  console.log(movieData.title);
});
