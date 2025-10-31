import numpy as np
from scipy.linalg import lu

# Input matrix dimensions
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print("Enter the entries in a single line separated by space:")

# Input matrix entries
entries = list(map(float, input().split()))
matrix = np.array(entries).reshape(r, c)

# Compute echelon form via LU decomposition
P, L, U = lu(matrix)

print("Input matrix:")
print(matrix)

print("Echelon form of the matrix (upper triangular U):")
print(U)

# Compute rank
rank = np.linalg.matrix_rank(matrix)
print("Rank of the matrix:", rank)
