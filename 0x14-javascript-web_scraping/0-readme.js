#!/usr/bin/node
// A script that reads a file and accepts argument as the filepath
const fs = require('fs');
const { argv } = require('process');
const filePath = argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err.message);
  } else {
    console.log(data.toString());
  }
});
