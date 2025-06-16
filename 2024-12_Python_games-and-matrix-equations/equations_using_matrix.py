def create_matrix(rows: int, cols: int, values: list) -> list:

    if len(values) != rows * cols:
        return "Given values didn't match matrix dimensions!"
    matrix = []
    x = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(values[x])
            x += 1
        matrix.append(row)

    return matrix

def display_matrix(matrix: list):

    for row in matrix:
        print(" ".join(map(str, row)))

def scalar_operation(matrix: list, scalar: int, operation: str) -> list:
    result = []
    for row in matrix:
        result_row = []
        for element in row:
            if operation == '+':
                result_row.append(element + scalar)
            elif operation == '-':
                result_row.append(element - scalar)
            elif operation == '*':
                result_row.append(element * scalar)
            elif operation == '/':
                result_row.append(element / scalar)
            else:
                return "Incorrect oeperation given!"
        result.append(result_row)
    return result

def matrix_multip(matrix_a: list, matrix_b: list) -> list:

    if len(matrix_a[0]) != len(matrix_b):
        return "Matrix columns didn't match matrixes rows!"

    result = []
    for row in matrix_a:
        result_row = []
        for col in range(len(matrix_b[0])):
            value = 0
            for i in range(len(matrix_b)):
                value += row[i] * matrix_b[i][col]
            result_row.append(value)
        result.append(result_row)

    return result

def transpose_matrix(matrix: list) -> list:

    transposed_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)

    return transposed_matrix

def determinant_3x3(matrix: list) -> list:

    if len(matrix) != 3 or len(matrix[0]) != 3:
        return "Matrix is not 3x3!"

    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

def inverse_3x3(matrix: list) -> list:
    det = determinant_3x3(matrix)
    if det == 0:
        return "Determinant = 0!"

    cofactors = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            submatrix = []
            for x in range(3):
                if x != i:
                    row = []
                    for y in range(3):
                        if y != j:
                            row.append(matrix[x][y])
                    submatrix.append(row)

            determinant_sub = (submatrix[0][0] * submatrix[1][1] - submatrix[0][1] * submatrix[1][0])
            cofactors[i][j] = ((-1) ** (i + j)) * determinant_sub

    adjugate = transpose_matrix(cofactors)

    inverse_matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(adjugate[i][j] / det)
        inverse_matrix.append(row)

    return inverse_matrix

matrix_a = create_matrix(rows= 3, cols= 3, values= [4, 7, 2, 3, 6, 1, 2, 5, 3])
matrix_b = create_matrix(rows= 3, cols= 3, values= [9, 8, 7, 6, 5, 4, 3, 2, 1])
matrix_c = create_matrix(rows= 3, cols= 3, values= [12, 15, 6, 9, 18, 21, 3, 6, 3])

print("Matricas skalārā saskaitīšana par 5: ")
display_matrix(scalar_operation(matrix= matrix_a, scalar= 5, operation= '+'))

print()
print("Matricas skalārā atņemšana par 1: ")
display_matrix(scalar_operation(matrix= matrix_a, scalar= 1, operation= '-'))

print()
print("Matricas skalārā dalīšana ar 3: ")
display_matrix(scalar_operation(matrix= matrix_c, scalar= 3, operation= '/'))

print()
print("Matricas skalārā reizināšana ar 2: ")
display_matrix(scalar_operation(matrix= matrix_a, scalar= 2, operation= '*'))

print()
print("Matricu ar matricu reizināšana:")
display_matrix(matrix_multip(matrix_a= matrix_a, matrix_b= matrix_b))

print()
print("Transponeta Matrica:")
display_matrix(transpose_matrix(matrix= matrix_a))

print()
print("Matricu izvadīšana: ")
display_matrix(matrix= matrix_a)

print()
print("3x3 inversa matrica")
display_matrix(inverse_3x3(matrix= matrix_a))
