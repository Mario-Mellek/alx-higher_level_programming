#!/usr/bin/node
const dict = require('./101-data').dict;
const sorted = {};

for (const key in dict) {
  const value = dict[key];
  if (value in sorted) {
    sorted[value].push(key);
  } else {
    sorted[value] = [key];
  }
}

console.log(sorted);
