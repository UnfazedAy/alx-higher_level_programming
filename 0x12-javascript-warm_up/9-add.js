#!/usr/bin/node
const { argv } = require('process');
const firstArgv = parseInt(argv[2]);
const secondArgv = parseInt(argv[3]);
function add (a, b) {
  return (a + b);
}
const sum = add(firstArgv, secondArgv);
console.log(sum);
