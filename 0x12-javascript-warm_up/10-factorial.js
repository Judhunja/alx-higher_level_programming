#!/usr/bin/node

function factorial (n) {
  let factorial = 1;
  n = Number(process.argv[2]);

  for (let i = 1; i <= n; i++) {
    factorial *= i;
  }
  console.log(factorial);
}

factorial();
