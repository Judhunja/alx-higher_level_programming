#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x, v in sorted(a_dictionary.items()):
        print(f"{x}: {v}")


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
