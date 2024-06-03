# ch6_1.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = 0.5
b = 1

# 绘制此函数图形
for C in range(-5, 6, 5):
    x = np.linspace(-4, 4, 100)
    y = a*x**2 + b*x + C
    plt.plot(x, y, color='b')
plt.grid()
plt.show()













