# ch22_6.py
from sympy import solve, Symbol
import numpy as np
rate1 = 0.01
rate2 = 0.99
coef1 = 2.6
coef2 = 3.0

a1 = Symbol('a1')
b1 = Symbol('b1')
eq1 = np.log(rate1/(1-rate1)) - coef1 * a1 - b1
eq2 = np.log(rate2/(1-rate2)) - coef2 * a1 - b1
data = solve((eq1, eq2))
print(f'a1 = {data[a1]:5.3f}')
print(f'b1 = {data[b1]:5.3f}')










