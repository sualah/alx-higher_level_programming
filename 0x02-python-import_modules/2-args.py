#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    arg_len = len(args) - 1
    txt = "arguments:"
    if arg_len == 0:
        txt = "arguments."
    elif arg_len == 1:
        txt = "argument:"
    else:
        txt = "arguments:"
    print("{} {}".format(arg_len, txt))
    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
