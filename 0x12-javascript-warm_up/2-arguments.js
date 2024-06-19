#!/usr/bin/node
const argsPassed = process.argv.length;
if (argsPassed === 3) {
  console.log('Argument found');
} else if (argsPassed > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
