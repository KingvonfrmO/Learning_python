def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0]) if matrix else 0

    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()
