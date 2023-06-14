#!/usr/bin/python3
def number_keys(a_dictionary):
    y = 0
    for x in a_dictionary.items():
        y += 1

    return y


if __name__ == "__main__":
    number_keys(a_dictionary)
