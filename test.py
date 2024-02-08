def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix row by row (each row separated by a newline, elements separated by space):")
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != cols:
                    raise ValueError(
                        "Incorrect number of elements in the row.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Invalid input. Please enter exactly {
                      cols} integers separated by spaces.")
    return matrix


def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    rows = int(input("Enter the number of rows in the matrices: "))
    cols = int(input("Enter the number of columns in the matrices: "))

    print("Matrix 1:")
    matrix1 = get_matrix_input(rows, cols)

    print("Matrix 2:")
    matrix2 = get_matrix_input(rows, cols)

    result_matrix = add_matrices(matrix1, matrix2)

    print("Resultant Matrix after addition:")
    print_matrix(result_matrix)


if __name__ == "__main__":
    main()
