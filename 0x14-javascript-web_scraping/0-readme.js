#!/usr/bin/node
// Script reads a file from the command-line argument and prints its content to the console

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, data) {
        if (err) {
                console.error(err);
                return;
                 }
        console.log(data);
});
