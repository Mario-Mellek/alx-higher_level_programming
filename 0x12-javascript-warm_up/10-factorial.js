#!/usr/bin/node
const firstArg = Number(process.argv[2]);

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

console.log(computeFactorial(firstArg));
