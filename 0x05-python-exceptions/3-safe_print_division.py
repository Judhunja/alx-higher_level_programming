#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result

    except (ValueError, ZeroDivisionError, TypeError):
        result = None
        return None

    finally:
        print("{}{}".format("Inside result: ", result))


if __name__ == "__main__":
    safe_print_division(a, b)
