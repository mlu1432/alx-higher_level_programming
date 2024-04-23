#!/usr/bin/node

const arg = process.argv[2];  // Directly access the first argument

if (arg === undefined)
{
	console.log('No argument');
}
else
{
	console.log(arg);
}