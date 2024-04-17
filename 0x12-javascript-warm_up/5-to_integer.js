#!/usr/bin/node
const arg = process.argv[2];
const numArg = parseInt(arg);

if (Number.isInteger(numArg)) {
  console.log(`My number: ${numArg}`);
} else {
  console.log('Not a number');
}
