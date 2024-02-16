#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in range(len(row))] for row in matrix]
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            new_matrix[i][k] = matrix[i][k] ** 2
    return new_matrix
