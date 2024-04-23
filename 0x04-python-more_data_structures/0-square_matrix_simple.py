def square_matrix_simple(matrix=[]):
    new_matrix = []
    row = len(matrix)
    column = len(matrix[0]) if matrix else 0

    for i in range(row):
        new_row = []
        for j in range(column):
            squared_value = matrix[i][j] ** 2
            new_row.append(squared_value)
        new_matrix.append(new_row)

    return new_matrix
