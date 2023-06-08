#!/usr/bin/python3
from sys import argv


def main():
    num = len(argv) - 1
    if num < 1:
        print("0 arguments.")
    elif num == 1:
        print("{} {}:\n{}: {}".format(num, "argument", num, argv[1]))
    elif num > 1:
        print("{} {}:".format(num, "arguments"))
        for x in range(1, num + 1):
            print("{}: {}".format(x, argv[x]))
    else:
        print("F")


if __name__ == "__main__":
    main()
