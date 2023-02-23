def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    result_matrix = [[0] * len(matrix1[0])] * len(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(add_matrices(matrix1, matrix2))
