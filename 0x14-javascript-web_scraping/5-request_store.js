#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if URL and file path are provided
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Check if request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: Status code ${response.statusCode}`);
    return;
  }

  // Write the response body to the file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`The content has been saved to ${filePath}`);
  });
});
