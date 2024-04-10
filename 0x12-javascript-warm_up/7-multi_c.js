#!/usr/bin/node
num = parseInt(process.argv[2]);
if (isNaN(num))
{
	console.log("Missing number of occurences");
}
else
{
	for (i = 0; i < num; i++)
	{
		console.log("C is fun");
	}
}
