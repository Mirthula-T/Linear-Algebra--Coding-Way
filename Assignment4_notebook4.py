import numpy as np

# Define the directed graph
graph = {
    'www.page1.com': ['www.page2.com', 'www.page3.com', 'www.page4.com'],
    'www.page2.com': ['www.page3.com','www.page4.com'],
    'www.page3.com': ['www.page1.com'],
    'www.page4.com': ['www.page1.com','www.page3.com']
}

# Get unique web pages
web_pages = sorted(list(graph.keys()))

# Define the size of the adjacency matrix
n = len(web_pages)

# Initialize the adjacency matrix with zeros
A = np.zeros((n, n))

# Fill the adjacency matrix based on the directed graph
for i, page in enumerate(web_pages):
    for link in graph[page]:
        j = web_pages.index(link)
        A[i, j] = 1

# Step 1: Formulate the importance of each page as a linear algebra problem
print("Step 1: Formulating the importance of each page as a linear algebra problem\n")
print("Adjacency Matrix (A):\n", A)

# Step 2: Verify that the solution to the problem is an Eigen Vector
eigenvalues, eigenvectors = np.linalg.eig(A.T)
index = np.argmax(np.isclose(eigenvalues, 1))
pagerank = np.real(eigenvectors[:, index])
print("\nStep 2: Verifying that the solution to the problem is an Eigen Vector\n")
print("Eigen Vector (Page Rank):", pagerank)

# Step 3: Rescale the Eigen Vector as a probability by ensuring the sum of all entries equals 1
pagerank /= np.sum(pagerank)
print("\nStep 3: Rescaling the Eigen Vector as a probability\n")
print("Page Rank (Importance of each page):", pagerank)


Step 1: Formulating the importance of each page as a linear algebra problem

Adjacency Matrix (A):
 [[0. 1. 1. 1.]
 [0. 0. 1. 1.]
 [1. 0. 0. 0.]
 [1. 0. 1. 0.]]

Step 2: Verifying that the solution to the problem is an Eigen Vector

Eigen Vector (Page Rank): [0.55529338 0.28479687 0.65184165 0.43086246]

Step 3: Rescaling the Eigen Vector as a probability

Page Rank (Importance of each page): [0.28879499 0.14811614 0.33900747 0.2240814 ]
