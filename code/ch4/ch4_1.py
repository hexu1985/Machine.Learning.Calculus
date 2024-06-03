# ch4_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.01, -5, 100)         # 左下角图
y = [1 / y for y in x]
plt.plot(x, y)

x = np.linspace(0.01, 5, 100)           # 右上角图
y = [1 / y for y in x]
plt.plot(x, y)

plt.axis([-5, 5, -5, 5])
plt.xticks(range(-5, 6, 1))
plt.yticks(range(-5, 6, 1))
plt.xlabel("x")
plt.ylabel("y")
plt.grid()                              
plt.show()




          



