#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    new_list = []
    try:
        for y in range(0, x):
            new_list.append(my_list[y])
            count += 1
        print(*new_list, sep="")
        return count
    except IndexError:
        print(*new_list, sep="")
        return count


if __name__ == "__main__":
    safe_print_list(my_list=[], x=0)
