#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for x in reversed(range(0, len(my_list))):
            print("{:d}".format(my_list[x]))


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
