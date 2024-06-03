# ch2_7.py
from sympy import *

x = Symbol('x')
f = 1 / x
print("右边趋近 0 = ", limit(f, x, 0))
print("左边趋近 0 = ", limit(f, x, 0, dir='-')) 













