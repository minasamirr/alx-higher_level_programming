#!/usr/bin/node

// 11-second_biggest.js

// Get the arguments passed to the script and convert them to integers
const numbers = process.argv.slice(2).map(Number);

// Check if no arguments are passed or if only one argument is passed
if (numbers.length === 0 || numbers.length === 1) {
    console.log(0);
} else {
    // Sort the numbers in descending order
    const sortedNumbers = numbers.sort((a, b) => b - a);
    // Print the second largest number
    console.log(sortedNumbers[1]);
}
