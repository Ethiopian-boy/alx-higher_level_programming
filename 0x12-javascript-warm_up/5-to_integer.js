#!/usr/bin/node

const arg = process.argv.slice(2);
const argInt = parseInt(arg[0]);
if (isNaN(argInt)) {
	console.log('Not a number');
} else if (typeof argInt === 'number') {
	console.log(`My number: ${argInt}`);
}
