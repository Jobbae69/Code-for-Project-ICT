# 1. Creating Matrices

# 1.a.i. 1st Matrix
matrix1 = [
    [10, 3, 5],  # Initials (J, C, E)
    [15, 1, 19]  # Second letters (O, A, S)
]

# 1.a.ii. 2nd Matrix
matrix2 = [
    [2, 0, 2],   # First 3 digits of student number (202)
    [6, 5, 7]    # Last 3 digits of student number (657)
]

# 1.b. Print both matrices
print("1st Matrix:")
for row in matrix1:
    print(row)

print("\n2nd Matrix:")
for row in matrix2:
    print(row)

# 2. Matrix Addition
matrix3 = [
    [
        matrix1[i][j] + matrix2[i][j]
        for j in range(3)
    ]
    for i in range(2)
]

print("\n3rd Matrix (Matrix Addition):")
for row in matrix3:
    print(row)

# 3. Scalar Multiplication
matrix4 = [
    [
        matrix1[i][j] * 2
        for j in range(3)
    ]
    for i in range(2)
]

print("\n4th Matrix (Scalar Multiplication of 1st Matrix by 2):")
for row in matrix4:
    print(row)

# 4. Matrix Transpose
matrix5 = [
    [matrix2[j][i] for j in range(2)]
    for i in range(3)
]

print("\n5th Matrix (Transpose of 2nd Matrix):")
for row in matrix5:
    print(row)

# 5. Matrix Multiplication (3rd matrix and 5th matrix)
# 2x3 matrix (matrix3) x 3x2 matrix (matrix5) = 2x2 matrix
matrix6 = [
    [
        sum(matrix3[i][k] * matrix5[k][j] for k in range(3))
        for j in range(2)
    ]
    for i in range(2)
]

print("\n6th Matrix (Matrix Multiplication of 3rd and 5th matrices):")
for row in matrix6:
    print(row)

# 6. Sum of All Elements in 3rd Matrix
sum_matrix3 = sum(sum(row) for row in matrix3)
print(f"\nSum of all elements in the 3rd matrix: {sum_matrix3}")

# 7. Zero Matrix
matrix7 = [
    [0 for _ in range(3)]
    for _ in range(2)
]

print("\n7th Matrix (2x3 Zero Matrix):")
for row in matrix7:
    print(row)
