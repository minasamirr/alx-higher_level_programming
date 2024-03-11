#!/usr/bin/node

// 8-square.js

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const size = parseInt(arg);

// Check if the conversion resulted in a valid positive integer
if (!isNaN(size) && size > 0) {
    // Loop to print the square
    for (let i = 0; i < size; i++) {
        console.log("X".repeat(size));
    }
} else {
    // Print "Missing size" if conversion failed or if the number is not positive
    console.log("Missing size");
}
