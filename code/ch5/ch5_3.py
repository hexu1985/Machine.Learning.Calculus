# ch5_3.py
import matplotlib.pyplot as plt
import numpy as np

a = 3
b = -12
c = 10

# 计算微分
x_min = 12 / 6

# 将x_min带入二次函数
y_min = a*x_min**2 + b*x_min + c

plt.text(x_min-0.25, y_min-1.2, '('+str((x_min))+','+str(y_min)+')')         
plt.plot(x_min, y_min, '-o', color='r')                

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# 导数
a_de = 6
b_de = -12
x_de = np.linspace(0, 4, 50)
y_de = a_de*x + b_de
plt.plot(x_de, y_de, color='g')         # 绘制导数
# 导数为0的(x, y)坐标
x_zero = 12 / 6
y_zero = 0.0
plt.text(x_zero-0.25, y_zero+1.2, '('+str((x_zero))+','+str(y_zero)+')')         
plt.plot(x_zero, y_zero, '-o', color='r')

plt.grid()
plt.show()














