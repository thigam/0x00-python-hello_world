#!/usr/bin/node
let args = process.argv.length - 2;
if (args == 0)
{
	message = "No argument";
}
else if (args == 1)
{
	message = "Argument found";
}
else
{
	message = "Arguments found";
}
console.log(message);
