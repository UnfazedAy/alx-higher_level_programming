#!/usr/bin/node
const { argv } = require('process');
const convertNumber = parseInt(argv[2]);
if (isNaN(convertNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertNumber}`);
}
