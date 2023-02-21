"""
Program to implement Newton-Raphson Power Flow

The inputs to this program will be the following:

1) Bus admittance matrix in either rectangular or polar form
2) The bus voltage phase angles in degrees (approximate values)
3) The bus voltage magnitudes
4) The slack bus
5

Things to be calculated are:
1) The x vector
2) The net Power and Reactive power vector
    *needs to be lamdified
3) The Jacobian
"""

import numpy as np
import math as m
import cmath as cm
import sympy as sym

row,col = input('Enter dimensions of Admittance matrix (no spaces): ')
row,col = int(row),int(col)

##prompt for style of complex number
polar = input('Are values polar(T/F): ')

## Getting elements of ybus admittance matrix
tmp = [[input('Enter elements of Ybus matrix one at a time: ') for i in range(row)]/
       for j in range(col)]

if polar =='T' or polar =='t':
    vals = []
    for r in tmp:
        for val in r:
            vals.append( cm.rect( int(val[0])), m.radians(int(val[-2])) ) )

else:
    ## assumption that is made that it is rectangular
    vals = []
    for r in tmp:
        for val in r:
            vals.append( complex(val) )


## Forming the bus admittance matrix
Ybus = np.reshape(vals, (row,col))
Ybus = sym.Matrix(Ybus)
