#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = Object.entries(dict).reduce((accum, [key, value]) => {
  if (!accum[value]) {
    accum[value] = [];
  }
  accum[value].push(key);
  return accum;
}, {});

console.log(newDict);
