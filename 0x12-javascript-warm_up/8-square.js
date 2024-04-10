#!/usr/bin/node
num = parseInt(process.argv[2]);
if (isNaN(num))
{
	console.log("Missing size");
}
else
{
	output = "";
	for (i = 0; i < num; i++)
	{
		for (j = 0; j < num; j++)
		{
			output += "X";
		}
		if (i < num - 1)
			output += "\n";
	}
	console.log(output);
}
