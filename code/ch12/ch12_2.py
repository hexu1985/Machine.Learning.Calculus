# ch12_2.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)
y = -x**3 + x**2
plt.plot(x, y, color='b')
plt.xlabel('Probability')
plt.ylabel('Likelihood')

plt.grid()
plt.show()













