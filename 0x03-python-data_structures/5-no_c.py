#!/usr/bin/python3
def no_c(my_string):
    noc = ['c', 'C']

    my_new = ''
    for x in my_string:
        if x not in noc:
            my_new += x

    return my_new


if __name__ == "__main__":
    no_c(my_string)
