#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let res = '';
        for (let j = 0; j < this.width; j++) {
          res += 'C';
        }
        console.log(res);
      }
    }
  }
}
module.exports = Square;
