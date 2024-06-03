# ch5_10.py
from sympy import *

x = Symbol('x')
f = Symbol('f')
f = 3*x**2 + 2*x + 10
print("f'(x) = ", f.diff())
print("f'(x) = ", diff(f, x))
















