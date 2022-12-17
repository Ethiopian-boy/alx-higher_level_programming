#!/usr/bin/node
/* a script that reads and prints the content of a file. */
const arg = process.argv;
const fs = require('fs');

fs.readFile(arg[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
