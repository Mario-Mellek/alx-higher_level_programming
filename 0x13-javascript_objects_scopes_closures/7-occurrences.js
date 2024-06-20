#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  list.forEach((ele) => {
    if (ele === searchElement) occurrences += 1;
  });
  return occurrences;
};
