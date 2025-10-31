import numpy as np

def is_diagonalizable(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    # If eigenvectors are linearly independent => diagonalizable
    rank = np.linalg.matrix_rank(eigenvectors)
    return rank == A.shape[0], eigenvalues, eigenvectors

def cayley_hamilton_verify(A):
    n = A.shape[0]
    # Find characteristic polynomial coefficients
    char_poly_coeffs = np.poly(A)  # Returns coefficients with highest degree first
    # Evaluate polynomial at A using Horner's method
    # p(A) = c0*A^n + c1*A^(n-1) + ... + cn*I where cn is constant term
    pA = np.zeros_like(A, dtype=float)
    for i, coeff in enumerate(char_poly_coeffs):
        power = n - i
        if power > 0:
            pA += coeff * np.linalg.matrix_power(A, power)
        else:
            pA += coeff * np.eye(n)
    return pA

# Input matrix
n = int(input("Enter the size of the square matrix: "))
print(f"Enter the {n*n} elements of the matrix row-wise (space separated):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(n, n)

# Check diagonalizability
diag, eigenvalues, eigenvectors = is_diagonalizable(A)
print(f"Eigenvalues:\n{eigenvalues}")

if diag:
    print("Matrix is diagonalizable.")
else:
    print("Matrix is NOT diagonalizable.")

# Cayley-Hamilton verification
result = cayley_hamilton_verify(A)
print("Matrix after applying its characteristic polynomial (should be close to zero matrix):")
print(result)

if np.allclose(result, np.zeros_like(A)):
    print("Cayley-Hamilton theorem is verified.")
else:
    print("Cayley-Hamilton theorem not verified.")
