#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print () - prints the rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let res = '';
      for (let j = 0; j < this.width; j++) {
        res += 'X';
      }
      console.log(res);
    }
  }

  // rotates the width for the height and vice-versa
  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }

  // multiplies the sides by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
