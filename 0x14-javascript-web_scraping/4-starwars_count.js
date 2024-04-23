#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Check if API URL is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

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
  const filmsData = JSON.parse(body);

  // Filter the films where Wedge Antilles (character ID 18) is present
  const filmsWithWedge = filmsData.results.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  // Print the number of films where Wedge Antilles is present
  console.log(filmsWithWedge.length);
});
