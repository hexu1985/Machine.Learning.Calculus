# ch6_4.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
c = -3

# 绘制此函数积分区间图形
x = np.linspace(0, 3, 100)
y = [c for cx in x]
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=3),
                 facecolor='lightgreen')
plt.grid()
plt.show()














