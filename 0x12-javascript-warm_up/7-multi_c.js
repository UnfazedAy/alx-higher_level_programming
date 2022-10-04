#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
