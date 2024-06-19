#!/usr/bin/node
const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstArg, secondArg);
