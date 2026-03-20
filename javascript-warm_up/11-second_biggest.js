#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2)
    .map(Number)
    .sort((a, b) => b - a);
  let i = 0;
  while (i < list.length && list[i] === list[0]) {
    i++;
  }
  if (list[i] === undefined) {
    console.log(0);
  } else {
    console.log(list[i]);
  }
}
