import numpy as np
r=int(input('enter no. of rows'))
c=int(input('enter no. of columns'))
print('enter the entries in single line seprated by space')
entries=list(map(int,input().split()))
matrix=np.array(entries).reshape(r,c)
print(matrix)
print(np.transpose(matrix))