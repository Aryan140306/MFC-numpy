import numpy as np
NR = int(input("Enter the number of rows:"))
NC = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")

# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
A = np.array(entries).reshape(NR, NC)
print("Matrix X is as follows:",'\n', A)

A_Inverse = np.linalg.inv(A)
Transpose_of_A_Inverse = np.transpose(A_Inverse)
Determinant_of_A = np.linalg.det(A)
Cofactor_of_A = np.dot(Transpose_of_A_Inverse, Determinant_of_A)

# For finding the cofactor of a Matrix
print("The Cofactor of a Matrix is:",'\n', Cofactor_of_A)

# For finding the Determinant a Matrix
print("The Determinant of a Matrix is:",'\n',Determinant_of_A)

# For finding the Adjoint of a Matrix
Adjoint_of_A = np.transpose(Cofactor_of_A)
print("The Adjoint of a Matrix is:",'\n',Adjoint_of_A)
