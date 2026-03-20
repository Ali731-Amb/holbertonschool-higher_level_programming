#!/usr/bin/node
const nb = parseInt(process.argv[2], 10);
if (isNaN(nb)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < nb) {
    console.log('C is fun');
    i++;
  }
}
