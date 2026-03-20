#!/usr/bin/node
const maVariable = parseInt(process.argv[2], 10);
if (isNaN(maVariable)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${maVariable}`);
}
