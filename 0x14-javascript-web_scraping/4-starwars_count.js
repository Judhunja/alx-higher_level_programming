#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let x = 0;
    for (const char of results) {
      if (char.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        x += 1;
      }
    }
    console.log(x);
  }
});
