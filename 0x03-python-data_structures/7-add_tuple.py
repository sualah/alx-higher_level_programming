#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_num = 0
    second_num = 0
    if len(tuple_a) >= 2:
        first_num += tuple_a[0]
        second_num += tuple_a[1]
    elif len(tuple_a) == 1:
        first_num += tuple_a[0]

    if len(tuple_b) >= 2:
        first_num += tuple_b[0]
        second_num += tuple_b[1]
    elif len(tuple_b) == 1:
        first_num += tuple_b[0]
    return first_num, second_num
