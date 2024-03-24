#!/usr/bin/node
const args = process.argv.slice(2).map(num => Number(num));
const numArgs = args.length;

if (numArgs <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  const secondLarge = sortedArgs[1];
  console.log(secondLarge);
}
