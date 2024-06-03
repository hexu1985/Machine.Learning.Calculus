# ch22_1.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 5.0, 21)
y = [4, 4, 5, 6, 8, 12, 18, 22, 35, 40, 45, \
     33, 28, 30, 32, 36, 38, 41, 35, 31, 20]

plt.scatter(x, y)
plt.xlabel('Quality')
plt.ylabel('rate')
plt.grid()
plt.show()
















