#!/usr/bin/python3
from sys import argv


def main():
    num = len(argv)
    sumof = 0
    for x in range(1, num):
        sumof += int(argv[x])

    if sumof == 0:
        print("0")
    else:
        print("{}".format(sumof))


if __name__ == "__main__":
    main()
