"""
Program to implement Newton-Raphson with nonlinear/linear system
of equations.

"""


import sympy as sym
import numpy as np



## Input from user
num = int(input('Enter the number of linear/nonlinear equations: '))
var_num = int(input('Enter the number of unique variables in system: '))

functions = [[input("Enter the equations one at a time: ") for i in range(1)] for j in range(num)]
var = sym.symbols([input('Enter the variables one at a time: ') for i in range(var_num)])

limit = float(input("\nEnter accuracy requirement: "))


## Convert functions into sympy stuff.
func = np.zeros((num,1))
for i in functions:
    func = np.vstack((func,sym.parse_expr(i[0], evaluate = False)))


## removing leading zeros
func = func[~np.all(func == 0, axis=1)]

## Creating Jacobi Matrix
J = sym.zeros(num,num)

for r in range(num):
    for c in range(num):
        J[r,c] = sym.diff(func[r][0], var[c])

## finding inverse of Jacobi matrix
Jinv = J.inv()

## creating callable functions
func = sym.Matrix(func)
f = sym.lambdify([var], func)
Jinvfunc = sym.lambdify([var], Jinv)

###########################################Solving Now##############################################################

## Getting initial guess from user
x_i = [[int(input('Enter initial guess one element at a time: ')) for i in range(1)] for j in range(2)]
x_i = sym.Matrix(x_i)

## Getting goal solution from user
y = [[int(input('Enter goal solution one element at a time: ')) for i in range(1)] for j in range(2)]
y = sym.Matrix(y)


print("\n\nSolution: ")

##Running iterative algorithm
while True:
    x = x_i + Jinvfunc(x_i[:])*(y - f(x_i[:]))
    print(x)
    if min(abs(x_i - x)) <=  limit and max(abs(x_i - x)) <= limit:
        break
    #update x_i
    x_i = x



input('\nPress a key to quit: ')
