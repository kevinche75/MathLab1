import numpy as np

def transform_to_triangular_matrix(matrix: np.ndarray, matrix_size: int):

    swaps_number = 0

    for i in range(matrix_size-1):

        max_column_value_index = np.argmax(np.abs(matrix[i:, i])) + i

        assert np.abs(matrix[max_column_value_index, i]) != 0, "Однозначаного решения нет"

        if i != max_column_value_index:
            matrix[[i, max_column_value_index]] = matrix[[max_column_value_index, i]]
            swaps_number +=1

        for j in range(i, matrix_size-1):
            if matrix[j+1, i] !=0:
                matrix[j+1] = matrix[j+1] - matrix[i] * matrix[j+1, i] / matrix[i, i]

    return swaps_number

def comp_determinant(matrix: np.ndarray, swaps_number: int, matrix_size: int):

    diagonal = [i for i in range(matrix_size)]
    determinant = np.prod(matrix[diagonal, diagonal])

    return determinant if swaps_number % 2 == 0 else -determinant

def comp_back_substitution(matrix: np.ndarray, matrix_size: int):

    decision_vector = np.zeros(matrix_size)

    for i in range(matrix_size-1, -1, -1):
        decision_vector[i] = (matrix[i, matrix_size] - np.sum(decision_vector * matrix[i, :matrix_size]))/matrix[i,i]
    
    return decision_vector

def comp_residual(source_matrix: np.ndarray, decision_vector: np.ndarray, matrix_size: int):
    
    return np.sum(source_matrix[:, :matrix_size] * decision_vector, axis = 1) - source_matrix[:, matrix_size]

def solve_by_ghaussian_method(source_matrix: np.array):

    matrix_size = source_matrix.shape[0]

    transformed_matrix = source_matrix.copy()

    swaps_number = transform_to_triangular_matrix(transformed_matrix, matrix_size)
    determinant = comp_determinant(transformed_matrix, swaps_number, matrix_size)
    decision_vector = comp_back_substitution(transformed_matrix, matrix_size)
    residual = comp_residual(source_matrix, decision_vector, matrix_size)

    return transformed_matrix, determinant, decision_vector, residual