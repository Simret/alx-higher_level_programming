#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';
request.get(api + process.argv[2], function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    const everything = JSON.parse(body);
    for (const ch of everything.characters) {
      request.get(ch, function (err, response, body) {
        const everything = JSON.parse(body);
        if (err) throw err;
        else if (response.statusCode === 200) { console.log(everything.name); }
      });
    }
  }
});
