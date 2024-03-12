#!/usr/bin/node
function add (a, b) {
  const e = a + b;
  console.log(e);
}

add(Number(process.argv[2]), Number(process.argv[3]));
