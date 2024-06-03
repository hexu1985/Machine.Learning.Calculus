# ch6_21.py
from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np
def fx(x):
    return (x**2-5*x+7)

def fy(x):
    return (2*x+1)

# 计算交叉点
r1 =  root(lambda x:fx(x)-fy(x), 0)     # 初始迭代值0
r2 =  root(lambda x:fx(x)-fy(x), 5)     # 初始迭代值5
print("x1 = %4.2f,  y1 = %4.2f" % (r1.x,fx(r1.x)))
print("x2 = %4.2f,  y2 = %4.2f" % (r2.x,fx(r2.x)))
# 绘制fx函数图形
x1 = np.linspace(0, 10, 40)
y1 = x1**2-5*x1+7                       # fx
plt.plot(r1.x, fx(r1.x), 'o')
plt.plot(x1, y1, '-', label='x**2-5*x+7')
# 绘制fy函数图形
x2 = np.linspace(0, 10, 40)
y2 = 2*x2+1                             # fy
plt.plot(r2.x, fy(r2.x), 'o')
plt.plot(x2, y2, '-', label='2*x+1')
plt.legend(loc='best')
plt.show()















