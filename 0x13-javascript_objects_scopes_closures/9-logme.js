#!/usr/bin/node

const arr = [];
exports.logMe = function (item) {
  const len = arr.length;
  console.log(`${len}: ${item}`);
  arr.push(item);
};
