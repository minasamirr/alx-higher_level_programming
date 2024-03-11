#!/usr/bin/node

// 7-multi_c.js

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const num = parseInt(arg);

// Check if the conversion resulted in a valid positive integer
if (!isNaN(num) && num > 0) {
    // Loop to print "C is fun" x times
    for (let i = 0; i < num; i++) {
        console.log("C is fun");
    }
} else {
    // Print "Missing number of occurrences" if conversion failed or if the number is not positive
    console.log("Missing number of occurrences");
}
