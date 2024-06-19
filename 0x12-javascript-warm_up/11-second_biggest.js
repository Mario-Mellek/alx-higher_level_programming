#!/usr/bin/node
const args = process.argv.slice(2);

function findSecondBiggest (args) {
  let first = 0;
  let second = 0;

  args.forEach((num) => {
    const value = Number(num);
    if (value > first) {
      [second, first] = [first, value];
    } else if (value > second && value < first) {
      second = value;
    }
  });

  console.log(second);
}

if (args.length < 2) {
  console.log(0);
} else {
  findSecondBiggest(args);
}
