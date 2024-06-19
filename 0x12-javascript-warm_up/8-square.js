#!/usr/bin/node
const firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  const size = Math.trunc(firstArg);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
