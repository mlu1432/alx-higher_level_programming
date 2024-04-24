#!/usr/bin/node
const { dict } = require('./101-data');

function sortOccurrences(inputDict)
{
	const newDict = {};

	// Iterate through each key-value pair in the original dictionary
	for (const [key, value] of Object.entries(inputDict))
	{
		// If the occurrence count does not exist as a key in the new dictionary, create it
		if (!newDict[value])
		{
			newDict[value] = [];
		}
		// Append the user ID to the list corresponding to the occurrence count
		newDict[value].push(key);
	}

	return newDict;
}

const sortedDict = sortOccurrences(dict);
console.log(sortedDict);