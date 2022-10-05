#!/usr/bin/node
exports.converter = function (base) {
  function conv (a) {
    return (parseInt(a).toString(base));
  }
  return conv;
};
