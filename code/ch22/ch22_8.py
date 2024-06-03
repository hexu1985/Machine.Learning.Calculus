# ch22_8.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 5.0, 1000)
y = [x for i in x]

for i in range(len(x)):
    f1 = 1 / (1 + np.exp(-22.976*x[i] + 64.332))
    f2 = 1 / (1 + np.exp(22.976*x[i] - 73.522))
    y[i] = f1 + f2 - 1

plt.plot(x, y)
plt.text(2.5, 0.5, 'f3(x)')
plt.text(3.2, 0.5, 'f4(x)')
plt.xlabel('Quality')
plt.ylabel('rate')
plt.grid()
plt.show()
















