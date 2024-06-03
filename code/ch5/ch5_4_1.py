# ch5_4_1.py
import matplotlib.pyplot as plt
import numpy as np

a = 3
b = -12
c = 10           

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# 绘制经过 x = 0, 1, 2, 3, 4 的切线
for x_loc in range(0, 5):
    y_loc = a*x_loc**2 + b*x_loc + c        # y坐标
    slope = 6 * x_loc - 12                  # 每一点的斜率
# x_new和y_new是经过切线的坐标, 只取3点
    x_new = [x_loc-1, x_loc, x_loc+1]
    y_new = [slope * (x - x_loc) + y_loc for x in x_new]
    plt.plot(x_new, y_new, color='g')
plt.grid()
plt.axis('equal')                          
plt.show()














