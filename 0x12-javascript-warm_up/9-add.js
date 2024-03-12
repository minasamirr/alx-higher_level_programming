#!/usr/bin/node

// 9-add.js

// Define a function named add with the prototype: function add(a, b)
function add (a, b) {
  // Return the addition of the two integers
  return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (!isNaN(arg1) && !isNaN(arg2)) {
  // Print the addition of the two integers using the add function
  console.log(add(arg1, arg2));
} else {
  // Print NaN if one or both arguments are not valid integers
  console.log('NaN');
}
