#!/usr/bin/node
// Script writes a string to a file

const fs = require('fs')
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf8', function (err) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Successfully wrote to the file');
});
