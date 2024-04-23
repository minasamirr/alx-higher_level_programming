#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Check if API URL is provided
if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Send a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Check if request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: Status code ${response.statusCode}`);
    return;
  }

  // Parse the response body to JSON
  const tasks = JSON.parse(body);

  // Create an object to store the count of completed tasks for each user ID
  const completedTasksCount = {};

  // Iterate over the tasks and count completed tasks for each user ID
  tasks.forEach(task => {
    // If task is completed (completed field is true), increment count for user ID
    if (task.completed) {
      if (completedTasksCount[task.userId]) {
        completedTasksCount[task.userId]++;
      } else {
        completedTasksCount[task.userId] = 1;
      }
    }
  });

  // Print the count of completed tasks for each user ID
  console.log(completedTasksCount);
});
