# ch6_6.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = -1

# 绘制此函数积分区间图形
x = np.linspace(0, 3, 1000)
y = -a*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=1),
                 facecolor='lightgreen')

x = np.linspace(-3, 0, 1000)
y = a*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-1)&(x<=0),
                 facecolor='lightblue')

plt.grid()
plt.show()














