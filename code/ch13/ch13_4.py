# ch13_4.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = 1/((2*np.pi)**0.5) * np.exp(-x**2/2)

plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-0.8)&(x<-0.6),
                 facecolor='green')

plt.grid()
plt.show()












