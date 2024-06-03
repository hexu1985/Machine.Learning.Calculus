# ch12_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)
y = x * x
plt.plot(x, y, color='b')
plt.xlabel('Probability')
plt.ylabel('Likelihood')

plt.grid()
plt.show()













