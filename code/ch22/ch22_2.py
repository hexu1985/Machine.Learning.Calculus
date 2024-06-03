# ch22_2.py
from sympy import solve, Symbol
import numpy as np
rate1 = 0.04
rate2 = 0.41
coef1 = 1
coef2 = 4.4

a1 = Symbol('a1')
b1 = Symbol('b1')
eq1 = np.log(rate1/(1-rate1)) - coef1 * a1 - b1
eq2 = np.log(rate2/(1-rate2)) - coef2 * a1 - b1
data = solve((eq1, eq2))
print(f'a1 = {data[a1]:5.3f}')
print(f'b1 = {data[b1]:5.3f}')










