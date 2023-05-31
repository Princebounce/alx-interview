#!/usr/bin/node


const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    film.characters.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});

