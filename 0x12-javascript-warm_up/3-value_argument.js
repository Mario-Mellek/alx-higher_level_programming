#!/usr/bin/node
const firstVar = process.argv[2];

if (!firstVar) {
  console.log('No argument');
} else {
  console.log(firstVar);
}
