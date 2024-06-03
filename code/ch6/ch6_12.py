# ch6_12.py
import matplotlib.pyplot as plt
import numpy as np

# 原始函数F(x)的系数
a = 1

# 绘制此函数积分区间图形
x = np.linspace(-1, 1, 1000)
y = a*x**2
plt.plot(x, y, color='aqua')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=1),
                 facecolor='lightpink')

x_line = np.linspace(0, 0.1, 2)
y_line = x_line

#绘制蓝色水平线
for i in range(10):
    x_line[0] = i*0.1
    x_line[1] = x_line[0] + 0.1
    y_line = [a*n**2 for n in x_line]
    y_line[1] = y_line[0]
    plt.plot(x_line, y_line, color='b')

#绘制蓝色垂直线
for i in range(10):
    x_line[0] = i*0.1 + 0.1
    x_line[1] = x_line[0]
    y_line[0] = 0
    y_line[1] = a*x_line[0]**2
    plt.plot(x_line, y_line, color='b')

plt.grid()
plt.show()














