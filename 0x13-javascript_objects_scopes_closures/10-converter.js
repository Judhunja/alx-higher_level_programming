#!/usr/bin/node

exports.converter = function (base) {
  return function toString (number) {
    return number.toString(base);
  };
};
