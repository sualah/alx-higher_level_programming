#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd = [[column ** 2 for column in row] for row in matrix]
    return sqrd
