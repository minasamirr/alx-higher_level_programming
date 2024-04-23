#!/usr/bin/node

const request = require("request");

// Get the URL to request from command line arguments
const url = process.argv[2];

// Check if URL is provided
if (!url) {
  console.error("Usage: ./2-statuscode.js <URL>");
  process.exit(1);
}

// Send a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
