#!/usr/bin/python3
def safe_print_integer(value):
    is_int = False
    try:
        print("{:d}".format(value))
        is_int = True
    except Exception:
        is_int = False
    return is_int
