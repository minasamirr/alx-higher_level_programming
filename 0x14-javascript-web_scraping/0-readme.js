#!/usr/bin/node

const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Check if file path is provided
if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Read the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print error object if an error occurred during reading
    console.error(err);
    return;
  }
  // Print the content of the file
  console.log(data);
});
