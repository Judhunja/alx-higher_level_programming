#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 || idx > len(my_list):
            return my_list
        else:
            my_list[idx] = element
            return my_list[idx]
