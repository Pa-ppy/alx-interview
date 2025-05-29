#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  const fetchCharacter = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (err, res, body) => {
      if (!err) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        fetchCharacter(index + 1);
      }
    });
  };

  fetchCharacter(0);
});
