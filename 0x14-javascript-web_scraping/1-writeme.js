#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if file path and string to write are provided
if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file-path> "<string-to-write>"');
  process.exit(1);
}

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // Print error object if an error occurred during writing
    console.error(err);
    return;
  }
  console.log('The file has been saved!');
});
