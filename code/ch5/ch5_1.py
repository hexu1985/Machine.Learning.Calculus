# ch5_1.py
import matplotlib.pyplot as plt
import numpy as np

a = 3
b = -12
c = 10

# 计算微分
x_min = 12 / 6

# 将x_min带入二次函数
y_min = a*x_min**2 + b*x_min + c

plt.text(x_min-0.25, y_min+0.5, '('+str((x_min))+','+str(y_min)+')')         
plt.plot(x_min, y_min, '-o', color='r')                
print(f'极小值 x 坐标 = {x_min}')
print(f'极小值 y 坐标 = {y_min}')

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# 绘制极小值的切线
x_tangent = np.linspace(0, 4, 50)
y_tangent = [y_min for element in x_tangent]
plt.plot(x_tangent, y_tangent, color='g')
plt.show()














