#!/usr/bin/node
function calleMeMoby (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++
  }
}
module.exports = { callMeMoby };
