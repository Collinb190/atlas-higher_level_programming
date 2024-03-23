#!/usr/bin/node
const argOne = process.argv[2];
const result = Number(argOne);

if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log(result);
}
