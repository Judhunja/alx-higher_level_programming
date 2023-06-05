#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str:s}"[39:67] + f"{str:s}"[107:112] + f"{str:s}"[:6]
print(str)
