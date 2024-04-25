This program calculates the eigenvalues and eigenvectors of a given matrix A using NumPy, then checks if the eigenvectors corresponding to distinct eigenvalues are linearly dependent or independent. Here's the algorithm breakdown:

1. Import the NumPy library.
2. Define matrix A.
3. Use NumPy's linalg.eig function to calculate the eigenvalues and eigenvectors of matrix A.
4. Print the eigenvalues and eigenvectors.
5. Concatenate the eigenvectors into a matrix V using np.column_stack.
6. Check if the eigenvectors are linearly dependent or independent:
   - Calculate the rank of matrix V using np.linalg.matrix_rank.
   - Compare the rank of V with the minimum dimension of V (rows or columns).
   - If the rank is less than the minimum dimension, the eigenvectors are linearly dependent.
   - Otherwise, they are linearly independent.
7. Print the result indicating whether the eigenvectors corresponding to distinct eigenvalues are linearly dependent or independent.

import numpy as np

# Define matrix A
A = np.array([[2,1,0],
              [1,3,-1],[0,-1,4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Concatenate eigenvectors into a matrix
V = np.column_stack(eigenvectors)

# Check if the eigenvectors are linearly dependent or independent
dependent = np.linalg.matrix_rank(V) < min(V.shape)

if dependent:
    print("Eigenvectors corresponding to distinct eigenvalues are linearly dependent.")
else:
    print("Eigenvectors corresponding to distinct eigenvalues are linearly independent.")
 
    Eigenvalues: [1.26794919 3.         4.73205081]
Eigenvectors:
[[-0.78867513 -0.57735027 -0.21132487]
 [ 0.57735027 -0.57735027 -0.57735027]
 [ 0.21132487 -0.57735027  0.78867513]]
Eigenvectors corresponding to distinct eigenvalues are linearly independent.
