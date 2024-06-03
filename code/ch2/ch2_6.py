# ch2_6.py
from sympy import *

x = Symbol('x')
f = 58 * (1 / 2)**x
print("result = ", limit(f, x, float('inf')))
print("result = ", limit(f, x, oo))











