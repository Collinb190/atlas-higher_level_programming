#!/usr/bin/node
const length = process.argv.length;
const myArgs = process.argv[2];

if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log(myArgs);
}
