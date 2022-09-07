#!/usr/bin/node

exports.callMeBoy = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
