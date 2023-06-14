#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_int = 0
    for x in set(my_list):
        my_int += x
    return my_int


if __name__ == "__main__":
    uniq_add(my_list=[])
