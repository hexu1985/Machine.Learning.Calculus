# ch21_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10000)               # 建立含10000个元素的数组
y = [(np.e**x - np.e**-x)/(np.e**x+np.e**-x) for x in x]
plt.axis([-5, 5, -1, 1])
plt.plot(x, y, label="Tanh function")

plt.legend(loc="best")                      # 建立图例
plt.grid()
plt.show()






