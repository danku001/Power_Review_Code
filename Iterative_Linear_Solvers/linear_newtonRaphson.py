"""
Newton-Raphson for linear system of equations.

Taylor series approximation to n = 1

f(x)  = \sum_{n=0}^1 f^{n}(a)/n! * (x - a)^n
      = f(a) + f'(a)*(x-a)
let a = x_i
let y = f(x) //goal solution

y = f(x_i) + f'(x_i)*(x - x_i)

x = (y - f(x_i)) *(f'(x_i))^{-1} + x_i

x = x_i + (y - f(x_i)) *(f'(x_i))^{-1}
"""
f = input('enter f(x): ')
fp = input("enter f'(x): ")
func = lambda x: eval(f)
fprime = lambda x: eval(fp)

x_i = float(input('enter initial guess for x: '))
y = float(input('enter goal solution: '))
lim = float(input('enter accuracy metric to terminate function: '))

x = 0

while True:
    x = x_i + (y - func(x_i))*1/(fprime(x_i))
    
    if abs(x_i - x) <= lim:
        break
    #update x_i
    x_i = x
    print('x: ',x)
    
