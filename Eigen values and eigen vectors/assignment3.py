

1.The matrix_inverse function takes a matrix as input and calculates its inverse using Gaussian elimination to reduce the augmented matrix to reduced row echelon form.

2. The matrix_multiply function multiplies two matrices together using nested loops.

3. An original matrix A is defined.

4. The inverse of A is calculated using the matrix_inverse function.

5. The product of A and its inverse is calculated using the matrix_multiply function.

6. Finally, the original matrix, its inverse, and their product are displayed.

This program essentially demonstrates how to find the inverse of a matrix and verify it by multiplying the original matrix with its inverse to get the identity matrix.




def matrix_inverse(matrix):
    n = len(matrix)
    # Augment the matrix with the identity matrix of the same size
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform row operations to get the reduced row echelon form
    for i in range(n):
        # Check if the diagonal element is zero
        if augmented_matrix[i][i] == 0:
            # If so, find a row below with a non-zero element in the same column and swap them
            for k in range(i+1, n):
                if augmented_matrix[k][i] != 0:
                    augmented_matrix[i], augmented_matrix[k] = augmented_matrix[k], augmented_matrix[i]
                    break
            else:
                # If no such row is found, skip this row
                continue
        
        # Make the diagonal element 1
        divisor = augmented_matrix[i][i]
        for j in range(n * 2):
            augmented_matrix[i][j] /= divisor
        
        # Make other elements in the same column 0
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(n * 2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]
    
    # Extract the right half of the augmented matrix (inverse of the original matrix)
    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix

def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Original matrix A
A = [
    [0,1,2],
    [1,0,3],
    [4,-3,8]
]

# Calculate the inverse of A
A_inverse = matrix_inverse(A)

# Multiply A with its inverse
product = matrix_multiply(A, A_inverse)

# Display the results
print("Original Matrix A:")
for row in A:
    print(row)

print("\nInverse of Matrix A:")
for row in A_inverse:
    print(row)

print("\nProduct of A and its inverse:")
for row in product:
    print(row)

Original Matrix A:
[0, 1, 2]
[1, 0, 3]
[4, -3, 8]

Inverse of Matrix A:
[-4.5, 7.0, -1.5]
[-2.0, 4.0, -1.0]
[1.5, -2.0, 0.5]

Product of A and its inverse:
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]









