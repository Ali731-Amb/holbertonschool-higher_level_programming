#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" ")
        print()
    print(" ".join([str(j) for j in i]))
