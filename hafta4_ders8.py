import sympy 
import math
from sympy import Symbol, solve, sin, Limit, S, oo

theta = Symbol('theta')
# math.sin(theta) 
""" 
There's an error here. Can't get mathematical sinus. Because theta isn't a mathematical magnitude.
Burada hata var. Matematiksel sinüs alamıyor. Çünkü theta matematiksel bir büyüklük değil.
"""

print(sympy.sin(theta)*sympy.sin(theta)) 

u = Symbol('u')
t = Symbol('t')
g = Symbol('g')

print(solve(u*sin(theta)-g*t, t)) 
# We find what is the value of t. / T değerinin ne olduğunu buluruz.

x = Symbol('x')
l = Limit(1/x, x, oo)
print(l.doit())

st = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')

st1 = st.subs({t:t1}) 
