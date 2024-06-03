# ch21_2.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10000)               # 建立含10000个元素的数组
y = [x if x >= 0 else 0 for x in x]
plt.axis([-5, 5, -5, 5])
plt.plot(x, y, label="ReLu function")

plt.legend(loc="best")                      # 建立图例
plt.grid()
plt.show()






