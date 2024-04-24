#!/usr/bin/node
const fs = require('fs');

// Extract command-line arguments
const [,, fileA, fileB, fileC] = process.argv;

// Function to concatenate files
function concatFiles(sourceFile1, sourceFile2, destinationFile)
{
	// Read the first file
	fs.readFile(sourceFile1, 'utf8', (err, data1) => {
		if (err) throw err;
		// Read the second file
		fs.readFile(sourceFile2, 'utf8', (err, data2) => {
			if (err) throw err;
			// Concatenate data1 and data2 then write to destination file
			fs.writeFile(destinationFile, data1 + data2, 'utf8', (err) => {
				if (err) throw err;
				});
			});
		});
}

// Call the function with the file paths
concatFiles(fileA, fileB, fileC);
