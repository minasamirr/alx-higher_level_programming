#!/usr/bin/node

// 5-to_integer.js

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const num = parseInt(arg);

// Check if the conversion resulted in a valid integer
if (!isNaN(num)) {
    // Print the integer
    console.log(`My number: ${num}`);
} else {
    // Print "Not a number" if conversion failed
    console.log("Not a number");
}
