import numpy as np

def gram_schmidt(V):
    """ Perform Gram-Schmidt process on matrix V whose columns are vectors """
    n, k = V.shape
    U = np.zeros((n, k))
    for i in range(k):
        # Start with the original vector
        vec = V[:, i]
        # Subtract projection on all previously found orthogonal vectors
        for j in range(i):
            vec -= np.dot(U[:, j], V[:, i]) * U[:, j]
        # Normalize the vector
        norm = np.linalg.norm(vec)
        if norm < 1e-10:  # Handle zero norm if vectors are linearly dependent
            U[:, i] = np.zeros_like(vec)
        else:
            U[:, i] = vec / norm
    return U

# Input number of vectors and their dimension
num_vecs = int(input("Enter number of vectors: "))
dim = int(input("Enter their dimension: "))

print("Enter each vector elements separated by space:")

vectors = []
for i in range(num_vecs):
    vec = list(map(float, input(f"Vector {i+1}: ").split()))
    vectors.append(vec)

# Create matrix with vectors as columns
V = np.array(vectors).T

# Perform Gram-Schmidt
orthonormal_basis = gram_schmidt(V)

print("Orthonormal basis vectors (columns):")
print(orthonormal_basis)
