#!/usr/bin/node

const argc = parseInt(process.argv[2], 10);
if (isNaN(argc)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${argc}`);
}
