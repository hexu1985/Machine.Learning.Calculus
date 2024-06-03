# ch6_8.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = -1
b = 2

# 绘制此函数积分区间图形
x = np.linspace(-2, 0, 1000)
y = -a*x**2 - b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-2)&(x<=0),
                 facecolor='lightblue')

x = np.linspace(0, 2, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=2),
                 facecolor='lightgreen')

x = np.linspace(2, 4, 1000)
y = -a*x**2 - b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=2)&(x<=4),
                 facecolor='lightblue')

plt.grid()
plt.show()














