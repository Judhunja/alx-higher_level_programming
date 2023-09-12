#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) { // Use a different variable (j) for the inner loop
        row += c;
      }
      console.log(row);
    }
  }
};
