#!/usr/bin/node

// 10-factorial.js

// Define a function named factorial
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }
  // Recursive case: compute factorial of n - 1 and multiply by n
  return n * factorial(n - 1);
}

// Get the first argument passed to the script and convert it to an integer
const arg = parseInt(process.argv[2]);

// Check if the argument is valid and compute factorial using the factorial function
if (!isNaN(arg)) {
  console.log(factorial(arg));
} else {
  // Print 1 if the argument is NaN
  console.log(1);
}
