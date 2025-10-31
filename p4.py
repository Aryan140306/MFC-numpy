import numpy as np
##Coefficient Matrix (A) Elements
print ("Enter the dimenssion of coefficients matrix (A):")
NR = int (input ("Enter the number of rows:"))
NC = int (input("Enter the number of columns:"))
print("Enter the elements of coefficients matrix (A)in a single line (separated by space):")
Coefficients Entries = list (map(float, input().split()))
Coefficient Matrix = np.array (Coefficients Entries).reshape (NR,NC)
print("Coefficient Matrix (A) is as follows:",'\n', Coefficient Matrix,"\n")
##Column Matrix (B) Elements
print("Enter the elements of column matrix (B) in a single line (separated by space):")
Column Entries = list(map(float, input().split()))
Column Matrix = np.array (Column Entries).reshape (NR, 1)
print("Column Matrix (B) is as follows:",'\n',Column Matrix,"\n")
#Solution of Homogeneous System of Equations using Gauss elimination method
Solution_of the_system_of_Equations = np.linalg.solve (Coefficient_Matrix, Column_Matrix)
print("Solution of the system of Equations using Gauss elimination method")
print(Solution_of_the_system_of_Equations)