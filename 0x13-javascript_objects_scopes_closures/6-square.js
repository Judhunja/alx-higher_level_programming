#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          row += c;
        } else {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
};
