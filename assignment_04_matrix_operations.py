# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(name):
    print(f"\n--- Enter Matrix {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Error: expected {cols} values, got {len(row_input)}. Try again.")
                continue
            row = [float(x) for x in row_input]
            matrix.append(row)
            break

    return matrix


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        # Format each value; use :g to avoid trailing .0 on whole numbers
        formatted = "  ".join(f"{val:g}" for val in row)
        print(formatted)


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def part_a_transpose():
    print("\n===== PART A: TRANSPOSE =====")
    matrix = read_matrix("A")
    print_matrix(matrix, "Original Matrix")

    result = transpose(matrix)
    print_matrix(result, "Transposed Matrix")


def part_b_addition():
    print("\n===== PART B: MATRIX ADDITION =====")
    print("Matrix A and Matrix B must have the same dimensions.")

    a = read_matrix("A")
    rows_a = len(a)
    cols_a = len(a[0])

    print(f"\nMatrix B must be {rows_a} x {cols_a} to match Matrix A.")
    while True:
        b = read_matrix("B")
        if len(b) == rows_a and len(b[0]) == cols_a:
            break
        print(f"Error: Matrix B must be {rows_a} x {cols_a}. Please re-enter.")

    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")

    result = add_matrices(a, b)
    print_matrix(result, "A + B")


def part_c_multiplication():
    print("\n===== PART C: MATRIX MULTIPLICATION =====")
    print("Number of columns in A must equal number of rows in B.")

    a = read_matrix("A")
    cols_a = len(a[0])

    print(f"\nMatrix B must have {cols_a} rows (to match columns of A).")
    while True:
        b = read_matrix("B")
        if len(b) == cols_a:
            break
        print(f"Error: Matrix B must have {cols_a} rows. Please re-enter.")

    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")

    result = multiply_matrices(a, b)
    print_matrix(result, "A x B")


def main():
    part_a_transpose()
    part_b_addition()
    part_c_multiplication()


if __name__ == "__main__":
    main()

# =============================================================================

