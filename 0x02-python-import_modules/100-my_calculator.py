#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    args_len = len(args) - 1
    result = 0
    if args_len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        op = args[2]
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = sub(a, b)
        elif op == '*':
            result = mul(a, b)
        elif op == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, op, b, result))
