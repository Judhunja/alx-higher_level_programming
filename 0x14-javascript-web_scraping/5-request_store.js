#!/usr/bin/node
const request = require('request');

const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
