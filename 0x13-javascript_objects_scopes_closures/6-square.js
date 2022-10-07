#!/usr/bin/node
const firstSquare = require('./5-square');
/**
 * class Square that defines a square and inherit from the first square
 * in task 5(5-square,js)
 **/
class Square extends firstSquare {
  /**
   * charPrint() - Prints Square with the specified character
   * @param {string} c The specified character.
   **/
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let res = '';
        for (let j = 0; j < this.height; j++) {
          res += c;
        }
        console.log(res);
      }
    }
  }
}
module.exports = Square;
