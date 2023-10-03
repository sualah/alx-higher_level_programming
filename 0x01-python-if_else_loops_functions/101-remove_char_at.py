#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str
    if n >= 0:
        copy = str[:n] + str[n+1:]
    return copy
