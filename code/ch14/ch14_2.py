# ch14_2.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D             # 绘制3D模块
import numpy as np

def f(x, y):                                        # 曲面函数
    return (np.power(x,2) + np.power(y, 2))

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-3, 3, 0.1)                           # 曲面 X 区间
Y = np.arange(-3, 3, 0.1)                           # 曲面 Y 区间
X, Y = np.meshgrid(X, Y)                            # 建立取样数据
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')           # 绘 3D 图
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')

plt.grid()
plt.show()
















