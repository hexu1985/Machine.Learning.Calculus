# ch6_18.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = -3
b = 18

# 绘制此函数积分区间图形
x = np.linspace(0, 6, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')

plt.grid()
plt.show()














