#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safely divides two numbers
    """

    try:
        result = a / b
    except Exception as err:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
