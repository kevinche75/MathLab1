import numpy as np

def transform_to_triangular_matrix(matrix: np.ndarray, method = "row"):

    matrix_size = matrix.shape[0]

    for i in range(matrix_size-1):

        if method == "row":

            max_row_value = np.argmax(np.abs(matrix[i, i:matrix_size])) + i
            matrix[:, [i, max_row_value]] = matrix[:, [max_row_value, i]]
        
        if method == "column":

            max_column_value = np.argmax(np.abs(matrix[i:, i])) + i
            matrix[[i, max_column_value]] = matrix[[max_column_value, i]]

        for j in range(i, matrix_size-1):
            if matrix[j+1, i] !=0:
                matrix[j+1] = matrix[j+1] - matrix[i] * matrix[j+1, i] / matrix[i, i]

def comp_determinant(matrix: np.ndarray):

    diagonal = [i for i in range(matrix.shape[0])]
    return np.prod(matrix[diagonal, diagonal])

def comp_back_substitution(matrix: np.ndarray):

    matrix_size = matrix.shape[0]

    result = np.zeros(matrix_size)

    for i in range(matrix_size-1, -1, -1):
        result[i] = (matrix[i, matrix_size] - np.sum(result * matrix[i, :matrix_size]))/matrix[i,i]
    
    return result