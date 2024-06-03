# ch16_1.py
from sympy import solve, symbols

a, b = symbols('a, b')
eq1 = 14*a + 6*b - 85
eq2 = 6*a + 3*b - 35
ans = solve((eq1, eq2))
print(ans)


















