#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
