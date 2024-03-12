#!/usr/bin/node

// 103-object_fct.js

// Define myObject with type and value properties
const myObject = {
  type: 'object',
  value: 12,
  // Define the incr function to increment the value property
  incr: function () {
    this.value++;
  },
};

console.log(myObject); // Print initial state of myObject

// Increment the value property using the incr function
myObject.incr();
console.log(myObject); // Print myObject after first increment

// Increment the value property again
myObject.incr();
console.log(myObject); // Print myObject after second increment

// Increment the value property once more
myObject.incr();
console.log(myObject); // Print myObject after third increment
