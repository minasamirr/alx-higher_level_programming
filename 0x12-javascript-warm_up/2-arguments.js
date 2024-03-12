#!/usr/bin/node

// 2-arguments.js

// Get the number of arguments passed to the script
const numArgs = process.argv.length;

// Check the number of arguments and print the appropriate message
if (numArgs === 2) {
	console.log('No argument');
} else if (numArgs === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
