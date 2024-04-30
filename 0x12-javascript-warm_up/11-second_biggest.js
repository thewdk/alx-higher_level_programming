#!/usr/bin/node
const args = process.argv.map(Number).slice(2, process.argv.length)
if (args <= 1) {
  console.log(0);
} else {
  const result = args.sort((a, b) => b - a);
  console.log(result[ 1]);
}

