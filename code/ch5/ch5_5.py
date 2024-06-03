# ch5_5.py
import matplotlib.pyplot as plt

a = 3
b = -12
c = 10           

# 绘制经过 x = 0-4 的40条切线
for counter in range(0, 41):
    x_loc = counter / 10
    y_loc = a*x_loc**2 + b*x_loc + c        # y坐标
    slope = 6 * x_loc - 12                  # 每一点的斜率
# x_new和y_new是经过切线的坐标, 只取3点
    x_new = [x_loc-1, x_loc, x_loc+1]
    y_new = [slope * (x - x_loc) + y_loc for x in x_new]
    plt.plot(x_new, y_new, color='g')
plt.grid()
#plt.axis('equal')                          # ch5_5_1.py此#符号取消
plt.show()














