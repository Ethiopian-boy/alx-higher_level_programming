#!/usr/bin/node

const args = process.argv.slice(2);
const argInt = args.map(s => parseInt(s));
if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  console.log(argInt.sort().reverse()[1]);
}
