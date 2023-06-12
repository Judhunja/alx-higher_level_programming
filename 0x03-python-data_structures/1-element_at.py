#!/usr/bin/python3
def element_at(my_list, idx):
    if len(my_list) == 0:
        return (None)
    elif idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        return my_list[idx]


if __name__ == "__main__":
    element_at(my_list, idx)
