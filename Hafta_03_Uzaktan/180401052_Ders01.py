from sympy import Symbol ,Limit
import pprint


x = Symbol('x')

St = 5*t**2 + 2*t + 8

t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St1 = St.subs({x: t1})
St1_delta = St.subs({x: t1 + delta_t})
print(Limit((St1_delta - St1) / delta_t, delta_t, 0).doit())
