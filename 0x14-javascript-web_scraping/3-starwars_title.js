#!/usr/bin/node
const request = require('request');

const epId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${epId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
