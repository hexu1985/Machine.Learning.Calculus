# ch6_2.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = 1
b = 1

# 绘制此函数积分区间图形
x = np.linspace(0, 6, 1000)
y = a*x + b
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=1)&(x<=5),
                 facecolor='lightgreen')
plt.grid()
plt.show()














