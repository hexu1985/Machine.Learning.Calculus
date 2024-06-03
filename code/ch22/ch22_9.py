# ch22_9.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 5.0, 1000)
y = [x for i in x]

for i in range(len(x)):
    f1 = 1 / (1 + np.exp(-0.828*x[i] + 4.006))
    f2 = 1 / (1 + np.exp(6.504*x[i] - 33.212))
    f3 = 1 / (1 + np.exp(-22.976*x[i] + 64.332))
    f4 = 1 / (1 + np.exp(22.976*x[i] - 73.522))
    y[i] = f1 + f2 - 1 + 0.3 * (f3 + f4 -1)

plt.plot(x, y)
plt.xlabel('Quality')
plt.ylabel('rate')
plt.grid()
plt.show()
















