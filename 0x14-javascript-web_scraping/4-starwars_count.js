#!/usr/bin/node

const request = require('request-promise-native');

async function getMoviesCountWithCharacter(apiUrl) {
  try {
    const response = await request(apiUrl);
    const movies = JSON.parse(response).results;
    
    // Count the number of movies where the character "Wedge Antilles" is present
    const moviesWithWedge = movies.filter(movie => {
      return movie.characters.some(character => character.endsWith('/18/'));
    });

    return moviesWithWedge.length;
  } catch (error) {
    console.error(error);
    return 0;
  }
}

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Check if API URL is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Invoke the function and print the result
getMoviesCountWithCharacter(apiUrl)
  .then(count => {
    console.log(count);
  })
  .catch(error => {
    console.error('Error:', error);
  });
