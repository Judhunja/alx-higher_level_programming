#!/usr/bin/node
const request = require('request');

const film = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${film}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const char of characters) {
      let names = [];

      request(char, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const data = JSON.parse(body);
          const name = data.name;
          names += name;
        }

        console.log(names);
      });
    }
  }
});
