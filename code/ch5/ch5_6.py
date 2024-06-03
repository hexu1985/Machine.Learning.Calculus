# ch5_6.py
import matplotlib.pyplot as plt
import numpy as np

# 二次函数的系数
a = -1
b = 50

# 计算微分
x_max = 50 / 2

# 将x_max带入二次函数
y_max = -x_max**2 + 50*x_max 

plt.text(x_max-5, y_max-50, '('+str((x_max))+','+str(y_max)+')')         
plt.plot(x_max, y_max, '-o', color='r')                

# 绘制此函数图形
x = np.linspace(0, 51, 50)
y = a*x**2 + b*x
plt.plot(x, y, color='b')

plt.grid()
plt.show()














