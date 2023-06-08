#!/usr/bin/python3
import hidden_4


def main():
    listof = dir(hidden_4)

    for x in listof:
        if x[0] != "_":
            print("{}".format(x))


if __name__ == "__main__":
    main()
