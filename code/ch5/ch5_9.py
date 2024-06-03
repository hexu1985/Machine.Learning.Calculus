# ch5_9.py
import matplotlib.pyplot as plt
import numpy as np

# 三次函数的系数
a = 1

# 绘制此函数图形
x = np.linspace(-2, 2, 100)
y = a*x**3
plt.plot(x, y, color='b')
plt.plot(0, 0, '-o', color='red')
plt.axis([-3, 3, -10, 10])
plt.grid()
plt.show()














