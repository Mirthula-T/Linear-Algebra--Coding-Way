# Original 3x3 matrix A
A = [[0,1,2],
     [1,0,3],
     [4,-3,8]]

# Function to calculate the inverse of a 3x3 matrix without using Python functions
def inverse(matrix):
    # Calculate the determinant of the matrix
    det = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
        matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
        matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    
    if det == 0:
        return None  # Matrix is singular, inverse does not exist
    else:
        inv_det = 1 / det
        # Calculate adjugate matrix
        adjugate = [
            [matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
             matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2],
             matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]],
            [matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2],
             matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
             matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]],
            [matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0],
             matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1],
             matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]]
        ]
        # Multiply adjugate matrix by 1/determinant
        inverse = [[adjugate[i][j] * inv_det for j in range(3)] for i in range(3)]
        return inverse

# Function to multiply two matrices
def matrixmul(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Calculate inverse of matrix A
A_inverse = inverse(A)

# Print original matrix A
print("Original matrix A:")
for row in A:
    print(row)

# Print inverse of matrix A
print("\nInverse of matrix A:")
for row in A_inverse:
    print(row)

# Calculate product of A and its inverse
product = matrixmul(A, A_inverse)

# Print the product
print("\nProduct of A and its inverse:")
for row in product:
    print(row)


   Original matrix A:
[0, 1, 2]
[1, 0, 3]
[4, -3, 8]

Inverse of matrix A:
[-4.5, 7.0, -1.5]
[-2.0, 4.0, -1.0]
[1.5, -2.0, 0.5]

Product of A and its inverse:
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]
