from numpy import matrix, linalg
import numpy as np

#Coefficient Matrix (A) Elements
print("Enter the dimension of coefficients matrix (A):")
NR = int(input("Enter the number of rows:"))
NC = int(input("Enter the number of columns:"))
print("Enter the elements of coefficients matrix (A) in a single line (separated by space):")
Coefficients_Entries = list(map(float, input().split()))
Coefficient_Matrix = np.array(Coefficients_Entries).reshape(NR,NC)
print("Coefficient Matrix (A) is as follows:",'\n', Coefficient_Matrix,"\n")

#Column Matrix (B) Elements
print("Enter the elements of column matrix (B) in a single line (separated by space):")
Column_Entries = list(map(float, input().split()))
Column_Matrix = np.array(Column_Entries).reshape(NR,1)
print("Column Matrix (B) is as follows:",'\n',Column_Matrix,"\n")

# Solution of Homogeneous System of Equations using GAUSS JORDAN
Inv_of_Coefficient_Matrix = linalg.inv(Coefficient_Matrix)
Solution_of_the_system_of_Equations = np.matmul(Inv_of_Coefficient_Matrix, Column_Matrix)
print("Solution of the system of Equations using GAUSS JORDAN")
print(Solution_of_the_system_of_Equations)
