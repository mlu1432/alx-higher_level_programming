#!/usr/bin/node
// script writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
