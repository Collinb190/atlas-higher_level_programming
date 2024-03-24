#!/usr/bin/node
function add (a, b) {
  return Number(a) + Number(b);
}

const args = process.argv.slice(2);
if (args.length !== 2) {
  console.log(NaN);
} else {
  const num1 = args[0];
  const num2 = args[1];
  const result = add(num1, num2);
  console.log(result);
}
