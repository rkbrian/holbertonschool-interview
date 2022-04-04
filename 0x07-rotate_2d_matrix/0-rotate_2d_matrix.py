#!/usr/bin/python3
"""
0-rotate_2d_matrix - input 'matrix' is a list of lists, the function will
return the matrix after rotate it 90 degrees clockwise. My method is to make
a new matrix 'lily', clear old data in 'matrix' and append data of 'lily'.
'new_row_len' and 'new_col_len' are the same for a square matrix.
"""


def rotate_2d_matrix(matrix):
    new_row_len = len(matrix)
    new_col_len = len(matrix[0])
    lily = []
    for i in range(new_col_len):
        lily.append(list(matrix[j][i] for j in reversed(range(new_row_len))))
    del matrix[:new_row_len]
    for i in range(new_col_len):
        matrix.append(lily[i])
