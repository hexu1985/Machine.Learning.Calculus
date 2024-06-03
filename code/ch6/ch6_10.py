# ch6_10.py
from sympy import *

x = Symbol('x')
f = -x**2 + 2*x
f1 = x**2 - 2*x
sec1 = integrate(f1, (x, -2, 0))
sec2 = integrate(f, (x, 0, 2))
sec3 = integrate(f1, (x, 2, 4))
print(sec1 + sec2 + sec3)

















