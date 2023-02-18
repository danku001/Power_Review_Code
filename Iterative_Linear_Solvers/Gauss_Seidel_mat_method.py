"""
Gauss-Seidel 
Matrix Form


x(i+1) = Mx(i) + D^(-1)*y

M = D^(-1)* (D - A)

Lower Triangle elements of A fill D
"""
import numpy as np

row = int(input('Enter the number of rows for matrix A: '))
col = int(input('Enter the number of cols for matrix A: '))
lim = float(input('Enter accuracy limit: '))

A = [[int(input('Enter the values of the A-matrix row-wise: ')) for i in range(col)] for j in range(row)]

x = [[int(input('Enter the initial guesses (x) row-wise: ')) for i in range(1)] for j in range(row)]

y = [[int(input('Enter the answers (y) row-wise: ')) for i in range(1)] for j in range(row)]


## Converting entered values into numpy arrays
A = np.asarray(A)
x = np.asarray(x)
y = np.asarray(y)


## Forming M and D
D = np.zeros((row,col))
D = D + np.tril(A,k=0) ##np.tril gets the lower triangle of a matrix

Dinv = np.linalg.inv(D)

M = np.matmul(Dinv, (D-A))

## Iteration
t = 0
while(True):
    t += 1
    new_col = np.matmul(M, x[:,[t-1]]) + np.matmul( Dinv, y )
    x = np.hstack((x, new_col))

    if abs( x[0,-1] - x[0,-2] ) <= lim:
        break
print('\n')
print(x)
