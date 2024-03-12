#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const sbiggest = arr.sort(function (l, s) { return s - l; })[1];
  console.log(sbiggest);
}
