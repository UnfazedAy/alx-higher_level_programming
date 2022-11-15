#!/usr/bin/node
/**
Writes a script that prints the title of a Star Wars movie,
where the episode number matches a given integer.
The first argument is the movie ID
You must use the Star wars API with the endpoint
https://swapi-api.hbtn.io/api/films/:id
**/
const { argv } = require('process');
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const episodeNum = argv[2];

request(apiUrl + episodeNum, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const Json = JSON.parse(body);
    console.log(Json.title);
  } else {
    console.log('Status: ', response.statusCode);
  }
});
