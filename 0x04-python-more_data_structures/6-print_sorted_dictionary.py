#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for x, v in sorted(a_dictionary.items()):
            print(f"{x}: {v}")

