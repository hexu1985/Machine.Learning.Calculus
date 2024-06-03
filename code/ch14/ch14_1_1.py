# ch14_1_1.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D             # 绘制3D模块
import numpy as np

def f(x, y):                                        # 曲面函数
    return (1 - (x**0.5)/2 - (y**0.5)/2)

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(0, 1, 0.01)                           # 曲面 X 区间
Y = np.arange(0, 1, 0.01)                           # 曲面 Y 区间
X, Y = np.meshgrid(X, Y)                            # 建立取样数据
ax.plot_surface(X, Y, f(X,Y), color='lightgreen', alpha=0.6)  

plt.axis('equal')
plt.grid()
plt.show()
















