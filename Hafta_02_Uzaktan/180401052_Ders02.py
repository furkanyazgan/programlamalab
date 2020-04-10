import sympy
from sympy import pprint
from sympy import Symbol
import sympy as sym
import sympy.plotting as syp
import sympy as sy
import matplotlib.pyplot as plt

sigma = Symbol('sigma')
mu = Symbol('mu')





x = Symbol('x')
part_1 = 1/(sym.sqrt(2*sym.pi*sigma*sigma))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function = part_1*part_2




print(pprint(my_gauss_function))

print(syp.plot(my_gauss_function.subs({mu:1,sigma:3}), (x, -10, 10), title='gauss'))

x_values = []
y_values = []
for value in range(-50,50):
    y = my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

plt.plot(x_values,y_values)