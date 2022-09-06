#!/usr/bin/node

const argInt = parseInt(process.argv[2]);
if (isNaN(argInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argInt; i++) {
    console.log('x'.repeat(argInt));
  }
}
