#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Show arguments')
parser.add_argument('arguments', nargs='*')
args = parser.parse_args()

if (len(args.arguments) == 1):
    print("{} argument:".format(1))
elif (len(args.arguments) == 0):
    print("{} arguments.".format(0))
else:
    print("{} arguments:".format(len(args.arguments)))

for i in args.arguments:
    print("{}: {}".format(args.arguments.index(i) + 1, i))
