#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_new[idx] = element
        return my_new


if __name__ == "__main__":
    new_in_list()
