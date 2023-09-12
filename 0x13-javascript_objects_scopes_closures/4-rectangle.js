#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const ex = this.height;
    this.height = this.width;
    this.width = ex;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
