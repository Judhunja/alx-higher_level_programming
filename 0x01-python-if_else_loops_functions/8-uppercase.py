#!/usr/bin/python3
def uppercase(str):
    chars = []
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        chars.append(i)
    print("{}".format(''.join(chars)))
