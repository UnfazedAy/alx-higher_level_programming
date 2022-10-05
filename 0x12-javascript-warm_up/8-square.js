#!/usr/bin/node
const { argv } = require('process');
const row = parseInt(argv[2]);
let result = '';
if (isNaN(row)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < row; j++) {
      result += 'X';
    }
    result += '\n';
  }
  console.log(result);
}
