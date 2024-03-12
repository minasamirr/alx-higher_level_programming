#!/usr/bin/node

// 101-call_me_moby.js

// Define the function callMeMoby
function callMeMoby(x, theFunction) {
  // Loop x times and execute theFunction each time
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Make the callMeMoby function visible from outside by exporting it
module.exports.callMeMoby = callMeMoby;
