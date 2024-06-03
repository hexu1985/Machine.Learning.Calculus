# ch8_1.py
from sympy import *

x = Symbol('x')
t = Symbol('t')
f1 = (x - 1) / 16
f2 = t / 16
print(integrate(f1, (x, 1, 4)))
print(integrate(f2, (t, 0, 3)))


















