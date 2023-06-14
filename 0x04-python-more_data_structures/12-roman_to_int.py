#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, ' M': 1000}

    total = 0
    prev = 0

    for x in reversed(roman_string):
        y = roman_numbers.get(x, 0)

        if y >= prev:
            total += y
        else:
            total -= y

        prev = y

    return total
