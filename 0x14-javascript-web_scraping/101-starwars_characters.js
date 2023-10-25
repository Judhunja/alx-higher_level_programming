#!/usr/bin/node
const request = require('request');

const film = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${film}`;

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const char of characters) {
      let names = [];
      await new Promise((resolve, reject) => {
        request(char, function (error, response, body) {
          if (error) {
            console.error(error);
            reject(error);
          } else {
            const data = JSON.parse(body);
            const name = data.name;
            names += name;
            resolve();
          }
          console.log(names);
        });
      });
    }
  }
});
