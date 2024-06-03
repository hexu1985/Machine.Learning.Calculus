# ch13_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = 1/((2*np.pi)**0.5) * np.exp(-x**2/2)

plt.plot(x, y, color='b')

plt.grid()
plt.show()













