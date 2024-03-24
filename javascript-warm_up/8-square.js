#!/usr/bin/node
const myVar = 'X';
const argOne = process.argv[2];
const squareSize = Number(argOne);

if (isNaN(squareSize)) {
  console.log('Missing size');
}
if (squareSize > 0) {
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += myVar;
    }
    console.log(row);
  }
}
