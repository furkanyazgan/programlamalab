from sympy import Symbol, exp, sqrt, pi, Integral

y = Symbol('y')
x = exp(-(y-10)**2/2) / sqrt(2*pi)
print(Integral(x,(y,11,12)).doit().evalf())