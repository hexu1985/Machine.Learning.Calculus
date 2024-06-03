# ch11_1.py
from sympy import *

x = Symbol('x')
f1 = (1/18)*x - (1/9)
y1 = integrate(f1, (x, 2, 6))

f2 = (-2/45)*x + (22/45)
y2 = integrate(f2, (x, 6, 11))
print(y1+y2)















