#!/usr/bin/python3
status = 1
for char in range(26, 0, -1):
    if (status == 1):
        print("{}".format(chr(char + 96)), end="")
        status = 0
    else:
        print("{}".format(chr(char + 64)), end="")
        status = 1
