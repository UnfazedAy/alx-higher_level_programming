#!/usr/bin/node
// A script that reads a file and accepts argument as the filepath
const fs = require('fs');
const { argv } = require('process');
const filePath = argv[2];

fs.readFile(filePath, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
