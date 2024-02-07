#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elem = 0
    try:
        for i in range(0, x):
            print(f"{my_list[i]}", end='')
            num_of_elem += 1
        print('')
    except Exception:
        print('')
    return num_of_elem
