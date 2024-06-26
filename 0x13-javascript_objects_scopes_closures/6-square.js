#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      console.log(square);
    }
  }
}
module.exports = Square;
