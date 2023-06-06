#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    rem = number % 10
    print("{}".format(rem), end='')
    return rem
