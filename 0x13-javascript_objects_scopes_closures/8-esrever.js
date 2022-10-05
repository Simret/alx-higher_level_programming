#!/usr/bin/node
exports.esrever = function (list) {
  const x = [];
  for (let i = list.length - 1; i >= 0; i--) {
    x[list.length - 1 - i] = list[i];
  }
  return x;
};
