#!/usr/bin/node
const request = require('request')
const movie = 'https://swapi-api.hbtn.io/api/films/'

request.get(movie + process.argv[2], function (err, response, body) {
  if (err) throw err
  if (response.statusCode === 200) {
    const everything = JSON.parse(body)
    const listch = []
    for (const charac of everything.characters) {
      listch.push(new Promise(function (resolve, reject) {
        request.get(charac, function (err, response, body) {
          if (err) throw err; if (response.statusCode === 200) { resolve(JSON.parse(body).name) } else { reject(Error('Unknown')) }
        })
      }))
    }
    Promise.all(listch).then(function (names) {
      names.forEach(function (name) {
        console.log(name)
      })
    })
  }
})
