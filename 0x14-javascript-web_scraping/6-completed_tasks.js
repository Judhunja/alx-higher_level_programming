#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    const data = JSON.parse(body);
    const userDict = {};
    for (const task of data) {
      if (task.completed === true) {
        if (userDict[task.userId]) {
          userDict[task.userId]++; // increment the value of the tasks done by the user
        } else {
          userDict[task.userId] = 1; // initialize the tasks done by the user to 1 if no previous task existed
        }
      }
    }
    console.log(userDict);
  }
});
