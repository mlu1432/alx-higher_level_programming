#!/usr/bin/node
// script reads a file from the command-line argument and prints its content to the console

const fs = require('fs');
const { fileURLToPath } = require('url');
const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
