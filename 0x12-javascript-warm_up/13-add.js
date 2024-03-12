#!/usr/bin/node

// 13-add.js

// Define the add function that returns the addition of two integers
function add(a, b) {
  return a + b;
}

// Make the add function visible from outside by exporting it
module.exports.add = add;
