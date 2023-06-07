#!/usr/bin/python3
for x in range(0, 8):
    for y in range(x + 1, 10):
        print("{:02}".format(x * 10 + y), end=", ")
print("{:02}".format(89))
