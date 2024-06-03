# ch12_3.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 1, 1000)
y = np.log(x)                       # e 为底数的 log()

plt.plot(x, y, color='b')

plt.grid()
plt.show()














