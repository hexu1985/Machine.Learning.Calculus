# ch6_16.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数f(x)的系数
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1*x**2 + c1
plt.plot(x, y1, color='b')
plt.text(3-0.4, a1*3**2+c1-0.5, 'f(x)')

# 原始函数g(x)的系数
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2*x**2 + b2*x + c2
plt.plot(x, y2, color='g')
plt.text(3-0.4, a2*3**2+b2*3+c2-0.5, 'g(x)')

plt.fill_between(x, y1=y1, y2=y2, where=(x>=-1)&(x<=2), facecolor='yellow')

plt.grid()
plt.show()














