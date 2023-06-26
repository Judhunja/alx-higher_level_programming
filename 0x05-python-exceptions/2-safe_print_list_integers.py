#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end='')
                count += 1

    except (IndexError, TypeError, ValueError):
        pass

    finally:
        print("")
        return count


if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
