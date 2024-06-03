# ch18_1.py
import matplotlib.pyplot as plt
import numpy as np

t = [85, 91, 76, 102, 68, 72, 66]           # 定义预估装潢天数
ave = np.mean(t)                            # 平均天数
x = np.linspace(0, 200, 200)                # 数组 x
y = np.linspace(0, 200, 200)                # 数组 y
min_x = 100                                 # 预估最初预估极值的 x
min_y = 100                                 # 预估最初预估极值的 y
for i in range(len(x)):                     # 从 0 到 200做测试
    sum = 0
    for j in range(len(t)):
        sum += (ave - x[i]) ** 2            # 计算平方和
    y[i] = sum 
    if y[i] < min_y:                        # 比较是否为误差最小平方和
        min_x = i
        min_y = y[i]

plt.plot(x, y)
plt.plot(min_x, min_y, '-o')
plt.text(min_x-20, min_y+2000, '('+str(round(min_x,1))+', '+str(round(min_y,5))+')')

plt.grid()
plt.show()



        
    

    



















