#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!Number.isNaN(num)) {
	  console.log('My number:', num);
} else {
	  console.log('Not a number');
}
