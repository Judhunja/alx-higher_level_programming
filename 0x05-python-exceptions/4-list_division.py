#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new_list = []
    for x in range(0, list_length):
        try:
            result = my_list_1[x] / my_list_2[x]

        except IndexError:
            result = 0
            print("out of range")

        except TypeError:
            result = 0
            print("wrong type")

        except ZeroDivisionError:
            result = 0
            print("division by 0")

        finally:
            new_list.append(result)

    return new_list


if __name__ == "__main__":
    list_division(my_list_1, my_list_2, list_length)
