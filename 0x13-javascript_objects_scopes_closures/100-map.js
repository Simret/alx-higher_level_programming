#!/usr/bin/node
const array = require('./100-data.js').list;
let i = 0;
console.log(array);
const x = array.map(a => a * i++);
console.log(x);
