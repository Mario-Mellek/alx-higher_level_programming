#!/usr/bin/node
let nbOArgs = 0;
exports.logMe = function (item) {
  console.log(`${nbOArgs++}: ${item}`);
};
