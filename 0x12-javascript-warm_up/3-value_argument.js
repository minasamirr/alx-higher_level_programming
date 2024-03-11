#!/usr/bin/node

// 3-value_argument.js

// Get the first argument passed to the script
const arg = process.argv[2];

// Check if argument exists and print it, otherwise print "No argument"
if (arg) {
	console.log(arg);
} else {
	console.log("No argument");
}
