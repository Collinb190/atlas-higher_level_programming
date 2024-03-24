#!/usr/bin/node
const args = process.argv.slice(2).map(num => Number(num));
const numArgs = process.argv.slice(2).length;

if (numArgs <= 1) {
  console.log(0);
}
const sortedArgs = args.sort((a, b) => b - a);
const secondLarge = sortedArgs[1];
console.log(secondLarge);
