#!/usr/bin/python3
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', nargs='*', type=int)
    args = parser.parse_args()
    sum = 0
    for i in args.num:
        sum += i
    print("{}".format(sum))

if __name__ == '__main__':
    main()
