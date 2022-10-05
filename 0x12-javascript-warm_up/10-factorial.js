#!/usr/bin/node
const { argv } = require('process');
const firstArgv = parseInt(argv[2]);
function factorial (n) {
  if (n === 0) {
    return 1;
  } else if (isNaN(n)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const result = factorial(firstArgv);
console.log(result);
