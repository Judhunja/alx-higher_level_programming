#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_new = my_list.copy()
    if my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        else:
            my_new[idx] = element
            return my_new
