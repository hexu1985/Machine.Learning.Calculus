# ch6_22.py
from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np
def fx(x):
    return (x**2 - 2)

def fy(x):
    return (-x**2 + 2*x + 2)

# 计算交叉点
r1 =  root(lambda x:fx(x)-fy(x), 0)     # 初始迭代值0
r2 =  root(lambda x:fx(x)-fy(x), 5)     # 初始迭代值5
print("x1 = %4.2f,  y1 = %4.2f" % (r1.x,fx(r1.x)))
print("x2 = %4.2f,  y2 = %4.2f" % (r2.x,fx(r2.x)))
# 绘制fx函数图形
x1 = np.linspace(-2, 3, 100)
y1 = x1**2 - 2                          # fx
plt.plot(r1.x, fx(r1.x), 'o')
plt.plot(x1, y1, '-', label='x**2 - 2')
# 绘制fy函数图形
x2 = np.linspace(-2, 3, 100)
y2 = -x2**2 + 2*x2 + 2                  # fy
plt.plot(r2.x, fy(r2.x), 'o')
plt.plot(x2, y2, '-', label='-x**2 + 2*x + 2')
plt.legend(loc='best')
plt.show()















