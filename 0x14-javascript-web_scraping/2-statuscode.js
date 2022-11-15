#!/usr/bin/node
/**
A script that display the status code of a GET request.
args: url => argv[2]
**/
const { argv } = require('process');
const request = require('request');
const url = argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
