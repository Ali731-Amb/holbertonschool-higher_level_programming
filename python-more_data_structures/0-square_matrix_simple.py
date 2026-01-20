#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_row = []
        for value in i:
            new_row.append(value ** 2)
        new_matrix.append(new_row)
    return new_matrix
