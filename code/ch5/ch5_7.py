# ch5_7.py
import matplotlib.pyplot as plt
import numpy as np

# 二次函数的系数
a = -3.5
b = 18.5
c = -5            

# 标记业绩点
x1 = 1
y1 = 10
plt.text(x1+0.05, y1-1, '('+str((x1))+','+str(y1)+')') 
plt.plot(x1, y1, '-o', color='g')
x2 = 2
y2 = 18
plt.text(x2+0.05, y2-1, '('+str((x2))+','+str(y2)+')') 
plt.plot(x2, y2, '-o', color='g')
x3 = 3
y3 = 19
plt.text(x3+0.05, y3+0.1, '('+str((x3))+','+str(y3)+')') 
plt.plot(x3, y3, '-o', color='g')

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

plt.grid()
plt.show()














