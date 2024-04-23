#!/usr/bin/node

function findSecondBiggest(numbers)
{
	let first = -Infinity, second = -Infinity;
	for (let number of numbers)
	{
		if (number > first)
		{
			second = first;
			first = number;
		}
		else if (number > second && number != first)
		{
			second = number;
		}
	}
	return second;
}

const args = process.argv.slice(2).map(Number);

if (args.length < 2)
{
	console.log(0);
}
else
{
    const secondBiggest = findSecondBiggest(args);
    console.log(secondBiggest === -Infinity ? 0 : secondBiggest);
}