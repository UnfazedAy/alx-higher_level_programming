#!/usr/bin/node
/**
A scriptt that akes in arguments as a file path and content
and writes in the content to the file
**/

const fs = require('fs');
const { argv } = require('process');
const filePath = argv[2];
const content = argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
