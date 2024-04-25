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