#!/usr/bin/node
const firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  const occurrences = Math.trunc(firstArg);
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
}
