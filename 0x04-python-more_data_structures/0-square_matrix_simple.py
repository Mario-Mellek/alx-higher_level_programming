#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = [[0 for j in range(len(matrix[i]))]
               for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared[i][j] = matrix[i][j] ** 2
    return squared
