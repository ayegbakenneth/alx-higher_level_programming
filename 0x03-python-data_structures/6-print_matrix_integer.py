#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        print(" ".join("{:d}".format(j)for i in j))
