#!/usr/bin/node
const myVarOne = 'C is fun';
const argOne = process.argv[2];
const result = Number(argOne);

if (isNaN(result)) {
  console.log('Missing number of occurrences');
}
if (result > 0) {
  let i = 0;
  while (i < result) {
    console.log(myVarOne);
    i++;
  }
}
