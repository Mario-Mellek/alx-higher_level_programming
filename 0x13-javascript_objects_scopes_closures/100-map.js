#!/usr/bin/node
const list = require('./100-data').list;
const mappedArr = list.map((ele, index) => {
  return ele * index;
});

console.log(list);
console.log(mappedArr);
