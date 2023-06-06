#!/usr/bin/python3
def fizzbuzz():
    fb = "FizzBuzz"
    f = "Fizz"
    b = "Buzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{fb} ", end='')
        elif i % 3 == 0:
            print(f"{f} ", end='')
        elif i % 5 == 0:
            print(f"{b} ", end='')
        else:
            print("{} ".format(i), end='')
