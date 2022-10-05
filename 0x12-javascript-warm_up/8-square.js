#!/usr/bin/node
const { argv } = require('process');
const row = parseInt(argv[2]);
if (isNaN(row)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < row; i++) {
    let res = '';
    for (let j = 0; j < row; j++) {
      res += 'X';
    }
    console.log(res);
  }
}
