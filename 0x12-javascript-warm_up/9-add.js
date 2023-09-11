#!/usr/bin/node

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];

  const num = Number(a) + Number(b);

  console.log(num);
}

add();
