#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let i = 1; i <= list.length; i++) {
    reversed.push(list[list.length - i]);
  }
  return reversed;
};
