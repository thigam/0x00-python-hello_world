#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            print("{}".format(i), end="")
        else:
            print("{}".format(chr(ord(i) - 32)), end="")

uppercase("hello")
