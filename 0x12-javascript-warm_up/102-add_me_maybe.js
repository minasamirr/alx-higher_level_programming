#!/usr/bin/node

// 102-add_me_maybe.js

// Define the function addMeMaybe
function addMeMaybe (number, theFunction) {
  // Increment the number by 1
  const newValue = number + 1;
  // Call theFunction with the incremented number as argument
  theFunction(newValue);
}

// Make the addMeMaybe function visible from outside by exporting it
module.exports.addMeMaybe = addMeMaybe;
