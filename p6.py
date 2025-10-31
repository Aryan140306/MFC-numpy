import numpy as np
from sympy import Matrix
#Coefficient Matrix (A) Elements
print("Enter the Dimenssion of Matrix (A):")
NR = int(input("Enter the Number of Rows:"))
NC = int (input("Enter the Number of Columns:"))
print("Enter the Elements of Matrix (A) in a single line (separated by space):")
Entries = list(map(float, input().split()))
A = np.array(Entries).reshape (NR, NC)
print("Matrix (A) is as follows:",'\n', A,"\n")
#Matrix A
A = Matrix (A)
# Null Space of A
NullSpace = A.nullspace() # Here NullSpace is a list
NullSpace = Matrix (NullSpace) # Here NullSpace is a Matrix
print("Null Space of a Matrix (A) is =",', NullSpace,'"\n")
#checking whether NullSpace satisfies the
#given condition or not as A * NullSpace = 0
# if NullSpace is null space of А
print("checking whether NullSpace satisfies the given condition", "\n",
"or not as A * NullSpace = 0", "\n",
"if NullSpace is null space of A")
print("Therefore, A * NullSpace =", A * NullSpace,"\n")
#Python Code for nullity of a Matrix.
# Number of Columns
NoC = A.shape[1]
# Rank of A
rank = A.rank ()
# Nullity of the Matrix
nullity = NoC - rank
print("Nullity of a Matrix (A) is =", nullity)