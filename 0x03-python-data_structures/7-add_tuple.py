#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = (tuple_a[0] if len(tuple_a) > 0 else 0)
        + (tuple_b[0] if len(tuple_b) > 0 else 0)
        b = tuple_b[1] if len(tuple_b) > 1 else 0
        ans = (a, b)
    elif len(tuple_b) < 2:
        a = (tuple_b[0] if len(tuple_b) > 0 else 0)
        + (tuple_a[0] if len(tuple_a) > 0 else 0)
        b = tuple_a[1] if len(tuple_a) > 1 else 0
        ans = (a, b)
    else:
        ans = (
            tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return ans


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
