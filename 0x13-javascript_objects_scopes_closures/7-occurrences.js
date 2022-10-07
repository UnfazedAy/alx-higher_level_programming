#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const word in list) {
    if (list[word] === searchElement) {
      count += 1;
    }
  }
  return count;
};
