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
      for (const charUrl of char.characters) {
        const urlSplit = charUrl.match(/\/(\d+)\/$/);
        if (urlSplit && urlSplit[1] === '18') {
          x++;
        }
      }
    }
    console.log(x);
  }
});
