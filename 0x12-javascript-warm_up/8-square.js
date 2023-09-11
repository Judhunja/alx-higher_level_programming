#!/usr/bin/node

const size = Number(process.argv[2]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let i = 0; i < size; i++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
