# ch5_2.py
import matplotlib.pyplot as plt
import numpy as np

a = -3
b = 12
c = -9

# 计算微分
x_max = 12 / 6

# 将x_max带入二次函数
y_max = a*x_max**2 + b*x_max + c

plt.text(x_max-0.25, y_max-0.7, '('+str((x_max))+','+str(y_max)+')')         
plt.plot(x_max, y_max, '-o', color='r')                
print(f'极大值 x 坐标 = {x_max}')
print(f'极大值 y 坐标 = {y_max}')

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# 绘制极小值的切线
x_tangent = np.linspace(0, 4, 50)
y_tangent = [y_max for element in x_tangent]
plt.plot(x_tangent, y_tangent, color='g')
plt.show()














